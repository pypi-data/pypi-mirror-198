# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import
import re
import colemen_utils as c

import copper_rabbit.settings as _settings
import copper_rabbit.settings.types as _t



def parse_integrity_error(err,result:_t._result_type):
    # print(f"err.detail: {err.detail}")
    # print(f"err.code: {err.code}")
    # print(f"err.orig: {err.orig}")
    # print(f"err.params: {err.params}")
    # print(f"err.args: {err.args}")
    # print(f"err.orig.args: {err.orig.args}")    
    emsg = err.orig.args[0]
    if "UNIQUE constraint failed:" in emsg:
        match = re.findall(r'UNIQUE constraint failed:\s*([a-zA-Z0-9_\.]*)',emsg)
        if len(match) > 0:
            m = match[0]
            datas = m.split(".")
            table = None
            col = None
            if len(datas) == 2:
                table = datas[0]
                col = datas[1]
            result.success = False
            result.public_response = _settings.datas.validation_errors_public_responses
            result.add_error(col,"This is already used.")
            result.add_internal_error("unique_error")
            # print(f"Table:{table}")
            # print(f"COLUMN:{col}")
    return result
