# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import
'''
    The Activity action methods

    ----------

    Meta
    ----------
    `author`: Colemen Atwood
    `created`: 03-17-2023 10:09:49
    `name`: Activity
    * @xxx [03-17-2023 10:09:49]: documentation for Activity
'''



import copper_rabbit.settings.types as _t
import copper_rabbit.schemas.Activity as _schemas
from copper_rabbit.models.Activity import Activity as _model
import copper_rabbit.support.actions as _x
import colemen_utils as _c


_PRIMARY_COLUMN_NAME="activity_id"
_DEFAULT_CREATE_SCHEMA=_schemas.CreateActivitiesSchema
_DEFAULT_UPDATE_SCHEMA=_schemas.UpdateActivitiesSchema
_DEFAULT_PUBLIC_SCHEMA=_schemas.PublicActivitiesSchema



def new_from_dict(data,include_model:bool=True)->_t._result_type:
    '''
        Create a new Activity log
        ----------

        Arguments
        -------------------------
        `data` {dict}
            A dictionary of data for creating the Activity log.

        Return {Result}
        ----------------------
        A Result instance.

        {
            success:True/False,
            public_response:"Here is the stuff",
            errors:{},
            data:{
                "schemas":[
                    {PublicActivitySchema}
                ],
                "models":[ActivityModel],
            },
        }
        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-17-2023 10:09:49
        `memberOf`: Activity
        `version`: 1.0
        `method_name`: new
        * @xxx [03-17-2023 10:09:49]: documentation for new
    '''
    return _x.new_x_from_dict(
        data,
        _DEFAULT_CREATE_SCHEMA,
        _DEFAULT_PUBLIC_SCHEMA,
        include_model=include_model,
    )

def get_by_hash_id(hash_id:str):
    return _x.get_by_col_x(
        value=hash_id,
        column_name="hash_id",
        model=_model,
        public_schema=_DEFAULT_PUBLIC_SCHEMA,
        include_model=True
    )

def get(include_model:bool=True,**kwargs):
    '''
        Retrieve Activitys by filtering their columns.
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
                    {PublicActivitySchema}
                ],
                "models":[ActivityModel],
            },
        }

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-17-2023 10:09:49
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
        Retrieve a Activity by its id.
        ----------

        Arguments
        -------------------------
        `primary_id` {str}
            The encoded activity_id to search for.

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
                    {PublicActivitySchema}
                ],
                "models":[ActivityModel],
            },
        }

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-17-2023 10:09:49
        `version`: 1.0
        `method_name`: get_by_id
        * @xxx [03-17-2023 10:09:49]: documentation for get_by_id
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
        update a Activity.
        ----------

        Arguments
        -------------------------
        `data` {dict}
            A dictionary of data to update the Activity with.

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
                    {PublicActivitySchema}
                ],
                "models":[ActivityModel],
            },
        }

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-17-2023 10:09:49
        `version`: 1.0
        `method_name`: update
        * @xxx [03-17-2023 10:09:49]: documentation for update
    '''
    # data['activity_id'] = _c.string.string_decode_int(data['activity_id'])
    return _x.update_x(
        data,
        update_schema=_DEFAULT_UPDATE_SCHEMA,
        public_schema=_DEFAULT_PUBLIC_SCHEMA,
        include_model=include_model,
        )

def soft_delete(primary_id:str,include_model:bool=False)->_t._result_type:
    '''
        Soft delete a Activity.
        ----------

        Arguments
        -------------------------
        `primary_id` {str}
            The encoded activity_id to search for.

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
                    {PublicActivitySchema}
                ],
                "models":[ActivityModel],
            },
        }

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-17-2023 10:09:49
        `version`: 1.0
        `method_name`: soft_delete
        * @xxx [03-17-2023 10:09:49]: documentation for soft_delete
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
        Undo the Soft deletion of a Activity.
        ----------

        Arguments
        -------------------------
        `primary_id` {str}
            The encoded activity_id to search for.

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
                    {PublicActivitySchema}
                ],
                "models":[ActivityModel],
            },
        }

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-17-2023 10:09:49
        `version`: 1.0
        `method_name`: undo_soft_delete
        * @xxx [03-17-2023 10:09:49]: documentation for undo_soft_delete
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
        Permanently delete a Activity
        ----------

        Arguments
        -------------------------
        `primary_id` {str}
            The encoded activity_id to search for.

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
                    {PublicActivitySchema}
                ],
                "models":[ActivityModel],
            },
        }

        Meta
        ----------
        `author`: Colemen Atwood
        `created`: 03-17-2023 10:09:49
        `version`: 1.0
        `method_name`: delete
        * @xxx [03-17-2023 10:09:49]: documentation for delete
    '''
    
    return _x.delete_x(
        primary_id=primary_id,
        model=_model,
        primary_column_name=_PRIMARY_COLUMN_NAME,
        public_schema=_DEFAULT_PUBLIC_SCHEMA,
        include_model=include_model,
        )

