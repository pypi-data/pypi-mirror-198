# -*- coding: utf8 -*-
from jennifer.agent import jennifer_agent
from jennifer.api.proxy import Proxy
import os


def _safe_get(attr, idx, default=None):
    try:
        return attr[idx]
    except IndexError:
        return default


class CursorProxy(Proxy):
    __slots__ = '__fetch_count__'

    def __init__(self, obj, host, port, paramstyle, conn):

        Proxy.__init__(self, obj)
        self.set('host', host)
        self.set('port', port)
        self.set('paramstyle', paramstyle)
        self.set('conn', conn)
        self.set('__fetch_count__', 0)

    def __enter__(self, *args, **kwargs):
        origin_cursor = Proxy.__enter__(self, *args, **kwargs)
        return CursorProxy(origin_cursor, self.host, self.port, self.paramstyle, self)

    def __exit__(self, *args, **kwargs):
        transaction = None

        try:
            agent = jennifer_agent()
            if agent is not None:
                removed = agent.recorder.db_recorder.remove_connection(self.conn)
                transaction = agent.current_transaction()
                if transaction is not None and removed:
                    transaction.profiler.db_close()
        except:
            pass

        try:
            Proxy.__exit__(self, *args, **kwargs)
        except Exception as e:
            if transaction is not None:
                transaction.profiler.end()
            raise e

        try:
            if transaction is not None:
                transaction.profiler.end()
        except:
            pass

        return

    # 변경 시 CursorProxy의 ConnectionProxy도 함께 변경
    def execute(self, *args, **kwargs):
        transaction = None
        agent = None
        operation = None

        try:
            agent = jennifer_agent()

            if agent is not None:
                transaction = agent.current_transaction()

            operation = _safe_get(args, 0) or kwargs.get('operation')
            parameters = _safe_get(args, 1) or kwargs.get('parameters')

            if transaction is not None:
                agent.recorder.db_recorder.active(self.conn)

            if transaction is not None and operation is not None:
                transaction.profiler.db_execute(self.host, self.port, operation, parameters, self.paramstyle)
        except Exception as e:
            print(os.getpid(), 'jennifer.exception', 'db.execute', e)

        result = None
        err = None

        try:
            try:
                result = self._origin.execute(*args, **kwargs)
            except Exception as e:
                err = e

            if err is not None and transaction is not None and operation is not None:
                transaction.profiler.sql_error(err)

        except:
            pass

        try:
            if transaction is not None and operation is not None:
                agent.recorder.db_recorder.inactive(self.conn)
                transaction.profiler.end()
        except:
            pass

        if err is not None:
            raise err

        return result

    def process_fetch(self, fetch, size, pass_size=False, is_fetch_one=False):
        transaction = None
        args = []
        agent = None

        try:
            agent = jennifer_agent()

            if agent is not None:
                transaction = agent.current_transaction()

            if pass_size:
                args = [size]
        except:
            pass

        if transaction is None:
            return fetch(*args)

        err = None
        ret = None

        try:
            try:
                agent.recorder.db_recorder.active(self.conn)
            except:
                pass

            ret = fetch(*args)

            if ret is not None:
                if is_fetch_one is True:
                    current_count = self.get('__fetch_count__')
                    self.set('__fetch_count__', current_count + 1)
                else:
                    transaction.profiler.db_fetch(len(ret))
            elif ret is None:
                fetch_count = self.get('__fetch_count__')
                if fetch_count is not None and fetch_count != 0:
                    transaction.profiler.db_fetch(fetch_count)

        except Exception as e:
            err = e

        try:
            agent.recorder.db_recorder.inactive(self.conn)
            transaction.profiler.end()
        except:
            pass

        if err is not None:
            raise err

        return ret

    @staticmethod
    def _debug_log(text):
        if os.getenv('JENNIFER_PY_DBG'):
            try:
                log_socket = __import__('jennifer').get_log_socket()
                if log_socket is not None:
                    log_socket.log(text)
            except ImportError as e:
                print(os.getpid(), 'jennifer.diagnostics', e)

    def fetchone(self):
        return self.process_fetch(self._origin.fetchone, 1, is_fetch_one=True)

    def fetchmany(self, size=None):
        pass_size = True
        if size is None:
            size = self._origin.arraysize
            pass_size = False
        return self.process_fetch(self._origin.fetchmany, size, pass_size)

    def fetchall(self):
        size = self.rowcount
        return self.process_fetch(self._origin.fetchall, size)

    def close(self):
        self._origin.close()


class ConnectionProxy(Proxy):

    def __init__(self, obj, host, port, paramstyle):
        Proxy.__init__(self, obj)
        self.set('host', host)
        self.set('port', port)
        self.set('paramstyle', paramstyle)

    def cursor(self, *args, **kwargs):
        return CursorProxy(self._origin.cursor(*args, **kwargs), self.host, self.port, self.paramstyle, self)

    # 변경 시 CursorProxy의 execute도 함께 변경
    def query(self, *args, **kwargs):
        transaction = None
        agent = None
        operation = None

        try:
            agent = jennifer_agent()

            if agent is not None:
                transaction = agent.current_transaction()

            operation = _safe_get(args, 0) or kwargs.get('operation')
            parameters = _safe_get(args, 1) or kwargs.get('parameters')

            if transaction is not None:
                agent.recorder.db_recorder.active(self)
                if operation is not None:
                    transaction.profiler.db_execute(self.host, self.port, operation, parameters, self.paramstyle)
        except:
            pass

        result = None
        err = None

        try:
            try:
                result = self._origin.query(*args, **kwargs)
            except Exception as e:
                err = e

            if err is not None and transaction is not None and operation is not None:
                transaction.profiler.sql_error(err)

        except:
            pass

        try:
            if transaction is not None and operation is not None:
                agent.recorder.db_recorder.inactive(self)
                transaction.profiler.end()
        except:
            pass

        if err is not None:
            raise err

        return result

    def __enter__(self, *args, **kwargs):
        origin_connection = Proxy.__enter__(self, *args, **kwargs)

        host = self.get('host')
        port = self.get('port')
        paramstyle = self.get('paramstyle')

        connection = ConnectionProxy(origin_connection, host, port, paramstyle)
        return connection

    def __exit__(self, *args, **kwargs):
        transaction = None

        try:
            agent = jennifer_agent()
            removed = agent.recorder.db_recorder.remove_connection(self)
            if agent is not None and removed:
                transaction = agent.current_transaction()
                if transaction is not None:
                    transaction.profiler.db_close()
        except:
            pass

        try:
            Proxy.__exit__(self, *args, **kwargs)
        except Exception as e:
            if transaction is not None:
                transaction.profiler.end()
            raise e

        try:
            if transaction is not None:
                transaction.profiler.end()
        except:
            pass

        return

    def close(self, *args, **kwargs):
        transaction = None

        try:
            agent = jennifer_agent()
            transaction = agent.current_transaction()
            removed = agent.recorder.db_recorder.remove_connection(self)
            if transaction is not None and removed:
                transaction.profiler.db_close()
        except:
            pass

        try:
            self._origin.close(*args, **kwargs)
        except Exception as e:
            if transaction is not None:
                transaction.profiler.end()
            raise e

        try:
            if transaction is not None:
                transaction.profiler.end()
        except:
            pass

        return


def register_database(db_module, connection_info):
    def _wrap_connect(connect):

        def handler(*args, **kwargs):
            agent = jennifer_agent()

            transaction = None
            host = None
            port = 0

            try:
                if agent.app_config.enable_sql_trace is not True:
                    return connect(*args, **kwargs)

                host, port, database = connection_info(*args, **kwargs)
                transaction = agent.current_transaction()

                if transaction is not None:
                    transaction.profiler.db_open(host, port, database)
            except:
                pass

            try:
                origin_connection = connect(*args, **kwargs)

                if transaction is not None:
                    connection = ConnectionProxy(origin_connection, host, port, db_module.paramstyle)
                else:
                    connection = origin_connection
            except Exception as e:
                if transaction is not None:
                    transaction.profiler.db_connection_error(e)
                    transaction.profiler.end()
                raise e

            try:
                if transaction is not None:
                    transaction.profiler.end()

                agent.recorder.db_recorder.add_connection(connection)
            except:
                pass

            return connection

        return handler

    original_connect = db_module.connect
    db_module.connect = _wrap_connect(db_module.connect)
    return original_connect
