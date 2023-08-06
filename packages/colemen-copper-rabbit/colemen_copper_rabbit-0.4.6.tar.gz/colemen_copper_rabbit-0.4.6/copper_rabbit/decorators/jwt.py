

from functools import wraps
from flask import Response
import copper_rabbit.settings as _settings
from copper_rabbit.actions.Session import get_session_auth
from flask import current_app


def jwt(
    optional=False,
    roles=None
    ):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            if optional is False:
                app = _settings.globe.app
                if app is not None:
                    session = get_session_auth(app)
                    if isinstance(session,Response):
                        return session
            return current_app.ensure_sync(fn)(*args, **kwargs)
            # return fn(*args, **kwargs)
        return decorator

    return wrapper


