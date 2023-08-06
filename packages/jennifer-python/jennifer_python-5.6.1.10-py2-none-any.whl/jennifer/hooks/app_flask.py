from jennifer.api.format import format_function
from jennifer.agent import jennifer_agent
from jennifer.wrap.wsgi import wrap_wsgi_app
from distutils.version import LooseVersion
import traceback

__hooking_module__ = 'flask'
__minimum_python_version__ = LooseVersion("2.7")
_original_flak_wsgi_app = None
_original_flask_dispatch_request = None

__target_version = None


def get_target_version():
    global __target_version
    return str(__target_version)


def unhook(flask_module):
    if _original_flak_wsgi_app is not None:
        flask_module.Flask.wsgi_app = _original_flak_wsgi_app

    if _original_flask_dispatch_request is not None:
        flask_module.Flask.dispatch_request = _original_flask_dispatch_request


def wrap_dispatch_request(origin):

    def handler(self):
        try:
            from werkzeug.exceptions import NotFound
        except ImportError:
            NotFound = None

        return_value = None
        err = None

        try:
            return_value = origin(self)
        except Exception as e:
            err = e

        if err is not None:
            try:
                current_tx = jennifer_agent().current_transaction()

                if current_tx is not None:
                    profiler = current_tx.profiler

                    if type(err) == NotFound:
                        profiler.not_found(err)
                    else:
                        if hasattr(err, '__traceback__'):
                            ex_result = traceback.format_exception(type(err), err, err.__traceback__)
                            ex_result = ''.join(ex_result)
                        else:
                            ex_result = str(err)

                        profiler.service_error("Service Error: " + ex_result)
            except:
                pass

            raise err

        return return_value

    return handler


def hook(flask_module):
    global _original_flak_wsgi_app
    global _original_flask_dispatch_request

    global __target_version
    __target_version = flask_module.__version__

    _original_flak_wsgi_app = flask_module.Flask.wsgi_app
    _original_flask_dispatch_request = flask_module.Flask.dispatch_request

    flask_module.Flask.wsgi_app = wrap_wsgi_app(flask_module.Flask.wsgi_app)
    flask_module.Flask.dispatch_request = wrap_dispatch_request(flask_module.Flask.dispatch_request)
