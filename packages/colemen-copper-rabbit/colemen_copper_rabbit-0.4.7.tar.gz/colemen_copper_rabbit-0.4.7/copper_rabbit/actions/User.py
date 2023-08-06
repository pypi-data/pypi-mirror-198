# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import
'''
    The User action methods

    ----------

    Meta
    ----------
    `author`: Colemen Atwood
    `created`: 03-16-2023 09:53:46
    `name`: User
    * @xxx [03-16-2023 09:54:06]: documentation for User
'''



import copper_rabbit.settings.types as _t
import copper_rabbit.schemas.User as _schemas
from copper_rabbit.models.User import User as _model
import copper_rabbit.support.actions as _x
from copper_rabbit.support import current_unix_timestamp
import copper_rabbit.support.Log as _log

_PRIMARY_COLUMN_NAME="user_id"
_DEFAULT_CREATE_SCHEMA=_schemas.CreateUsersSchema
_DEFAULT_UPDATE_SCHEMA=_schemas.UpdateUsersSchema
_DEFAULT_PUBLIC_SCHEMA=_schemas.PublicUsersSchema



def new_from_dict(data,include_model:bool=True)->_t._result_type:
    '''
        Create a new User log
        ----------

        Arguments
        -------------------------
        `data` {dict}
            A dictionary of data for creating the User log.

        Return {Result}
        ----------------------
        A Result instance.

        {
            success:True/False,
            public_response:"Here is the stuff",
            errors:{},
            data:{
                "schemas":[
                    {PublicUserSchema}
                ],
                "models":[UserModel],
            },
        }
        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-17-2023 09:30:52
        `memberOf`: User
        `version`: 1.0
        `method_name`: new
        * @xxx [03-17-2023 09:30:52]: documentation for new
    '''

    from copper_rabbit.actions.Session import new_from_dict as _new_session
    _log.add("Registering new user.","info")
    result = _x.new_x_from_dict(
        data,
        _DEFAULT_CREATE_SCHEMA,
        _DEFAULT_PUBLIC_SCHEMA,
        include_model=True,
    )

    if result.success is True:
        _log.add("Successfully registered user.","success")
        _log.add("Generating session","info")
        sres = _new_session(
            {
                "tk_type":"access",
                "user_id":result.models.user_id
            })
        if sres.success is True:
            _log.add("Successfully Generated new session.","success")
            result.set_key("jwt",sres.get_key("jwt"))
    # TODO []: create a new session/token
    #     mdl:_model = result.models

    return result


def login(email:str,password:str,include_model:bool=True):
    _log.add("Attempting User Login","info")
    result = _x.get_by_col_x(
        value=email,
        column_name="email",
        model=_model,
        public_schema=_DEFAULT_PUBLIC_SCHEMA,
        include_model=True
    )
    if result.success is True:
        mdl:_model = result.models
        _log.add("Successfully located user by email","success")
        if mdl.password == password:
            _log.add("Successfully logged in User","success")
            _log.add("Generating session","info")
            from copper_rabbit.actions.Session import new_from_dict as _new_session
            sres = _new_session(
                {
                    "tk_type":"access",
                    "user_id":result.models.user_id
                })

            if sres.success is True:
                _log.add("Successfully Generated new session.","success")
                result.set_key("jwt",sres.get_key("jwt"))
            # TODO []: generate new session/token
            # print(f"successfully logged in")
        else:
            _log.add("Failed","success")
            result.success = False
            result.public_response = "Password or email is incorrect"
    if result.success is False:
        result.success = False
        result.public_response = "Password or email is incorrect"
    return result

def get(include_model:bool=True,**kwargs):
    '''
        Retrieve Users by filtering their columns.
        ----------

        Arguments
        -------------------------
        [`include_model`=True] {bool}
            Add the "models" key to the result data.

        Return {Result}
        ----------------------
        A Result instance.

        {
            success:True/False,
            public_response:"Here is the stuff",
            errors:{},
            data:{
                "schemas":[
                    {PublicUserSchema}
                ],
                "models":[UserModel],
            },
        }

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-16-2023 11:53:40
        `version`: 1.0
        `method_name`: get
        * @TODO []: documentation for get
    '''
    return _x.get_x(
        model=_model,
        public_schema=_DEFAULT_PUBLIC_SCHEMA,
        include_model=include_model,
        **kwargs
        )

def get_by_id(primary_id:str,include_model:bool=False)->_t._result_type:
    '''
        Retrieve a User by its id.
        ----------

        Arguments
        -------------------------
        `primary_id` {str}
            The encoded user_id to search for.

        [`include_model`=True] {bool}
            Add the "models" key to the result data.


        Return {Result}
        ----------------------
        A Result instance.

        {
            success:True/False,
            public_response:"Here is the stuff",
            errors:{},
            data:{
                "schemas":[
                    {PublicUserSchema}
                ],
                "models":[UserModel],
            },
        }

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-16-2023 11:55:48
        `version`: 1.0
        `method_name`: get_by_id
        * @xxx [03-16-2023 11:57:25]: documentation for get_by_id
    '''
    return _x.get_x_by_id(
        primary_id=primary_id,
        primary_column_name=_PRIMARY_COLUMN_NAME,
        model=_model,
        public_schema=_DEFAULT_PUBLIC_SCHEMA,
        include_model=include_model,
        )

def update(data:dict,include_model:bool=False)->_t._result_type:
    '''
        update a User.
        ----------

        Arguments
        -------------------------
        `data` {dict}
            A dictionary of data to update the User with.

        [`include_model`=True] {bool}
            Add the "models" key to the result data.


        Return {Result}
        ----------------------
        A Result instance.

        {
            success:True/False,
            public_response:"Here is the stuff",
            errors:{},
            data:{
                "schemas":[
                    {PublicUserSchema}
                ],
                "models":[UserModel],
            },
        }

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-16-2023 11:55:48
        `version`: 1.0
        `method_name`: update
        * @xxx [03-16-2023 11:57:25]: documentation for update
    '''
    return _x.update_x(
        data,
        update_schema=_DEFAULT_UPDATE_SCHEMA,
        public_schema=_DEFAULT_PUBLIC_SCHEMA,
        include_model=include_model,
        )

def soft_delete(primary_id:str,include_model:bool=False)->_t._result_type:
    '''
        Soft delete a User.
        ----------

        Arguments
        -------------------------
        `primary_id` {str}
            The encoded user_id to search for.

        [`include_model`=True] {bool}
            Add the "models" key to the result data.


        Return {Result}
        ----------------------
        A Result instance.

        {
            success:True/False,
            public_response:"Here is the stuff",
            errors:{},
            data:{
                "schemas":[
                    {PublicUserSchema}
                ],
                "models":[UserModel],
            },
        }

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-16-2023 11:55:48
        `version`: 1.0
        `method_name`: soft_delete
        * @xxx [03-16-2023 11:57:25]: documentation for soft_delete
    '''
    return _x.soft_delete_x(
        primary_id=primary_id,
        model=_model,
        primary_column_name=_PRIMARY_COLUMN_NAME,
        public_schema=_DEFAULT_PUBLIC_SCHEMA,
        include_model=include_model,
        )

def undo_soft_delete(primary_id:str,include_model:bool=False)->_t._result_type:
    '''
        Undo the Soft deletion of a User.
        ----------

        Arguments
        -------------------------
        `primary_id` {str}
            The encoded user_id to search for.

        [`include_model`=True] {bool}
            Add the "models" key to the result data.


        Return {Result}
        ----------------------
        A Result instance.

        {
            success:True/False,
            public_response:"Here is the stuff",
            errors:{},
            data:{
                "schemas":[
                    {PublicUserSchema}
                ],
                "models":[UserModel],
            },
        }

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-16-2023 11:55:48
        `version`: 1.0
        `method_name`: undo_soft_delete
        * @xxx [03-16-2023 11:57:25]: documentation for undo_soft_delete
    '''
    return _x.undo_soft_delete_x(
        primary_id=primary_id,
        model=_model,
        primary_column_name=_PRIMARY_COLUMN_NAME,
        public_schema=_DEFAULT_PUBLIC_SCHEMA,
        include_model=include_model,
        )

def delete(primary_id:str,include_model:bool=False)->_t._result_type:
    '''
        Permanently delete a User
        ----------

        Arguments
        -------------------------
        `primary_id` {str}
            The encoded user_id to search for.

        [`include_model`=True] {bool}
            Add the "models" key to the result data.


        Return {Result}
        ----------------------
        A Result instance.

        {
            success:True/False,
            public_response:"Here is the stuff",
            errors:{},
            data:{
                "schemas":[
                    {PublicUserSchema}
                ],
                "models":[UserModel],
            },
        }

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-16-2023 11:55:48
        `version`: 1.0
        `method_name`: delete
        * @xxx [03-16-2023 11:57:25]: documentation for delete
    '''
    
    return _x.delete_x(
        primary_id=primary_id,
        model=_model,
        primary_column_name=_PRIMARY_COLUMN_NAME,
        public_schema=_DEFAULT_PUBLIC_SCHEMA,
        include_model=include_model,
        )

