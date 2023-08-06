# pylint: disable=line-too-long
# pylint: disable=unused-import
# pylint: disable=import-outside-toplevel
'''
    Module containing the backend logging apparatus.

    Meta
    ----------
    `author`: Colemen Atwood
    `created`: 01-24-2023 09:52:03
    `memberOf`: __init__
    `version`: 1.0
    `method_name`: Log
    * @xxx [01-24-2023 09:52:30]: documentation for Log
'''



import colemen_utils as c
import time
import json
from flask import request
import copper_rabbit.settings as _settings

LOG = []
DATA = {
    "log":[]
}

def result_array_logs()->list:
    '''
        Retrieve the current requests log array for the result object.
        If the server is NOT in test mode, this will always return an empty array.
        ----------

        Return {list}
        ----------------------
        A list of message logs.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 01-24-2023 10:06:52
        `version`: 1.0
        `method_name`: result_array_logs
        * @TODO []: documentation for result_array_logs
    '''
    # @Mstep [IF] if the server is not in test mode.
    if _settings.control.test_mode is False:
        # @Mstep [RETURN] return an empty list.
        return []
    # @Mstep [ELSE] if the server is in test mode.
    else:
        # @Mstep [return] return the log array
        return LOG

def request_log()->str:
    '''
        Retrieve the current request log as a compressed base64 string.
        ----------

        Return {str}
        ----------------------
        The request log JSON as a compressed base64 string

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 01-24-2023 10:02:54
        `version`: 1.0
        `method_name`: request_log
        * @TODO []: documentation for request_log
    '''
    import zlib
    import base64
    # text = b"Python Pool!" * 100
    bstring = bytes(json.dumps(LOG), 'utf-8')
    compressed = zlib.compress(bstring)
    print(f"compressed:{compressed}")

    # return str(compressed)
    return str(base64.b64encode(compressed))

def add(message,style="info"):
    '''
        Add a message to the current request log.
        ----------

        Arguments
        -------------------------
        `message` {any}
            The message of the log

        [`style`="info"] {str}
            The style or type of this log.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 01-24-2023 09:53:02
        `memberOf`: __init__
        `version`: 1.0
        `method_name`: add
        * @xxx [01-24-2023 09:54:09]: documentation for add
    '''
    data = {
        "timestamp":time.time(),
        "message":message,
    }

    LOG.append(data)
    if _settings.control.log_to_console is True:
        c.con.log(message,style)

