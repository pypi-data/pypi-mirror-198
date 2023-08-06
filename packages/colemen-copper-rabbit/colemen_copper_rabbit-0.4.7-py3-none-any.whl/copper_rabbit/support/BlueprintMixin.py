# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import

import colemen_utils as c
from flask import abort,request

from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import NoResultFound,IntegrityError
import copper_rabbit.support.Log as _log
from copper_rabbit.support.get_header_cookie import get_header_cookie
from copper_rabbit import settings as _s
from copper_rabbit.settings.globe import Response,result as gres
# from copper_rabbit.settings.datas import internal_server_errors



class BlueprintMixin:
    """Blueprint Copper Rabbit Mixin"""



    def coming_soon(self):
        '''
            If this decorator is used, the route will automatically respond with a coming soon message.
            ----------

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 03-20-2023 10:03:03
            `memberOf`: BlueprintMixin
            `version`: 1.0
            `method_name`: coming_soon
            * @xxx [03-20-2023 10:03:41]: documentation for coming_soon
        '''

        def decorator(func):
            gres().coming_soon()
            abort(gres().response)

            return func

        return decorator



    def activity(self,
        hash_id:str,
        title:str,
        description:str,
        url:str,
        crud_type:str,
        good_bad:int=3,
        desirability:int=3,
        extroversion:int=3,
        user_responsibility:int=2,
        daily_limit:int=None,
        probation_duration_days:int=None,
        is_deprecated:bool=False,
        is_primary:bool=False,
        is_live:bool=True,
        is_error:bool=False,

        general_blocking:bool=True,
        blackhole:bool=True,
        ):
        '''
            Decorator to register/retrieve an activity from the database.

            Once retrieved the activity is tested to see if the route is allowed to be executed.
            ----------

            Arguments
            -------------------------


            `hash_id` {str}
                The id used to externally identify this row.

            `title` {str}
                The title of this activity

            `description` {str}
                A brief description of the activity

            `url` {str}
                The API route/url that this activity belongs to

            `crud_type` {str}
                The crud operation performed by this activity.

            [`good_bad`=3] {int}
                A score from 1-5 for how good or bad this activity is.

            [`desirability`=3] {int}
                A score from 1-5 of how desirable the activity is.

            [`extroversion`=3] {int}
                A score from 1-5 for how extroverted the activity is.

            [`user_responsibility`=2] {int}
                A score from 1-3 of how responsible the user is for the activity occuring.

            [`daily_limit`=None] {int}
                How many times per day the activity can be performed before requests are rejected. Defaults to null meaning infinite.

            [`probation_duration_days`=None] {int}
                How many days the requestor will be prohibited from this activity, defaults to null.

            [`is_deprecated`=False] {bool}
                1 if the activity should no longer be available for the api to find.

            [`is_primary`=False] {bool}
                1 if this activity is single successful

            [`is_live`=True] {bool}
                1 if this activity is ready to be executed through the api.

            [`is_error`=False] {bool}
                1 if this activity defines an error.

            [`general_blocking`=True] {bool}
                If False this route will be accessible through maintenance and coming soon modes.

                This will only run on primary activities.

            [`blackhole`=True] {bool}
                If False this route will be accessible regardless of if the requestor is blocked.

                This will only run on primary activities.


            Return {type}
            ----------------------
            return_description

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 03-20-2023 08:32:39
            `memberOf`: BlueprintMixin
            `version`: 1.0
            `method_name`: activity
            * @TODO []: documentation for activity
        '''

        def decorator(func):
            if is_primary is True:
                if general_blocking is True:
                    _test_general_blocking()
                if blackhole is True:
                    _test_blackhole(url)

            data = {
                "hash_id":hash_id,
                "title":title,
                "description":description,
                "url":url,
                "good_bad":good_bad,
                "desirability":desirability,
                "extroversion":extroversion,
                "user_responsibility":user_responsibility,
                "daily_limit":daily_limit,
                "probation_duration_days":probation_duration_days,
                "crud_type":crud_type,
                "is_deprecated":is_deprecated,
                "is_primary":is_primary,
                "is_live":is_live,
                "is_error":is_error,
            }

            result = _test_activity(data)

            return func

        return decorator


def _test_blackhole(url):
    block = False
    # TODO []: check if the requestor is blocked from this url
    # TODO []: check if the requestor is blocked from all requests.

def _test_general_blocking():
    '''
        Test if the server is in maintenance or coming soon mode.

        If the server is in one of these modes, it will abort the request.

        ----------

        Return {bool}
        ----------------------
        If the request is not aborted, it returns True.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-20-2023 10:21:01
        `memberOf`: BlueprintMixin
        `version`: 1.0
        `method_name`: _test_general_blocking
        * @xxx [03-20-2023 10:22:31]: documentation for _test_general_blocking
    '''
    block = False
    if _s.control.maintenance_mode:
        _log.add("Server is in maintenance mode","info")
        block = True

    if _s.control.coming_soon_mode:
        _log.add("Server is in coming soon mode","info")
        block = True

    bypass = get_header_cookie(_s.control.bypass_name)
    if bypass is not None:
        _log.add("Bypass cookie/header was located.","info")
        # TODO []: use a bypass token to confirm the requestor.
        block = False

    if block is True:
        if _s.control.maintenance_mode:
            _log.add("Server is in maintenance mode, generating response","info")
            gres().maintenance_mode()
            # @Mstep [] abort the request with the maintenance response
            abort(gres().coming_soon_mode)
        if _s.control.coming_soon_mode:
            _log.add("Server is in coming soon mode, generating response","info")
            gres().coming_soon()
            # @Mstep [] abort the request with the coming soon response
            abort(gres().response)
    return True



def _test_activity(data):
    '''
        Test to confirm that the activity is allowed to be performed.

        ----------

        Arguments
        -------------------------
        `data` {dict}
            A dictionary of activity data.

        Return {type}
        ----------------------
        return_description

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-20-2023 09:18:23
        `version`: 1.0
        `method_name`: _test_activity
        * @TODO []: documentation for _test_activity
    '''
    hash_id = data['hash_id']
    mdl = _retrieve_activity(data)
    if mdl is False:
        mdl = _register_new_activity(data)


    # TODO []: confirm that the activity is allowed to execute (doesn't exceed the daily limit)
    return True

def _retrieve_activity(data):
    '''
        Attempt to retrieve an activity from the database.
        ----------

        Arguments
        -------------------------

        `data` {dict}
            A dictionary of activity data.

        Return {type}
        ----------------------
        The Activity model if successful, False otherwise.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-20-2023 09:19:23
        `version`: 1.0
        `method_name`: _retrieve_activity
        * @xxx [03-20-2023 09:20:22]: documentation for _retrieve_activity
    '''
    from copper_rabbit.actions.Activity import get_by_hash_id
    hash_id = data['hash_id']
    result = get_by_hash_id(hash_id)
    if result.success is True:
        _log.add(f"Successfully located activity: {hash_id}","success")
        mdl = result.models
        return mdl
    else:
        return False

def _register_new_activity(data):
    '''
        Attempt to register a new activity with the database.

        ----------

        Arguments
        -------------------------
        `data` {dict}
            A dictionary of activity data.

        Return {Model,bool}
        ----------------------
        The new Activity model if successful, False otherwise.

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-20-2023 09:20:32
        `version`: 1.0
        `method_name`: _register_new_activity
        * @xxx [03-20-2023 09:21:15]: documentation for _register_new_activity
    '''
    from copper_rabbit.actions.Activity import new_from_dict
    hash_id = data['hash_id']
    title = data['title']
    _log.add(f"Registering new activity with database: {hash_id} {title}","info")
    result = new_from_dict(data)
    # @Mstep [IF] if the submission fails
    if result.success is False:
        _log.add(f"Failed to Register new activity with database: {hash_id} {title}","error")
        # @Mstep [] abort the request.
        abort(gres().internal_server_error())
    else:
        _log.add(f"Successfully Registered new activity with database: {hash_id} {title}","error")
        mdl = result.models
        return mdl