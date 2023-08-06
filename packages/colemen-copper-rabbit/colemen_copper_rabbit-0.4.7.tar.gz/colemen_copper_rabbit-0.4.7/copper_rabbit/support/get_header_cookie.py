from typing import Union
import colemen_utils as _c
from flask import request
# import copper_rabbit.settings as _settings







def get_header_cookie(name)->Union[str,None]:
    '''
        Attempt to retrieve a cookie, if it is not found, search for a header by the same name.
        ----------

        Arguments
        -------------------------
        `name` {str}
            The name to search for.

        Return {any}
        ----------------------
        The cookie/header value if successful, None otherwise

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-20-2023 09:32:51
        `version`: 1.0
        `method_name`: get_header_cookie
        * @xxx [03-20-2023 09:33:52]: documentation for get_header_cookie
    '''
    result = None
    cookie = _c.obj.get_arg(request.cookies,[name],None)
    if cookie is not None:
        result = cookie

    if cookie is None:
        header = request.headers.get(name,None)
        if header is not None:
            result = header
    return result













