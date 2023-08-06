# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import
'''
    The ActivitiesSchema Schemas

    ----------

    Meta
    ----------
    `author`: Colemen Atwood
    `created`: 03-17-2023 10:09:46
    `memberOf`: schemas
    `name`: ActivitiesSchema
'''


from __future__ import annotations
from typing import Iterable, List, Union

from marshmallow import Schema, fields, validate, ValidationError,EXCLUDE
import colemen_utils as c


# from copper_rabbit.settings.globe import base as _base
import copper_rabbit.settings as _settings
from copper_rabbit.models.Activity import Activity
from copper_rabbit.custom_fields import StatusCode,CrudType,RequestMethod,RequestLog,HashidPrimary,DeletedTimestamp
from copper_rabbit.support.BaseSchema import BaseSchema
from copper_rabbit.support.timestamp import current_unix_timestamp








class CreateActivitiesSchema(BaseSchema):
    '''
        The CreateActivitiesSchema class


        Meta
        ----------
        `@author`: Colemen Atwood
        `@created`: 03-17-2023 10:09:46
        `@memberOf`: ActivitiesSchema
    '''
    class Meta:
        model = Activity
        include_relationships = True
        load_instance = True
        unknown=EXCLUDE

    hash_id = fields.String(allow_none=False, required=False, validate=[validate.Length(1,255)])
    title = fields.String(allow_none=False, required=True, validate=[validate.Length(1,255)])
    '''The title of this activity'''
    description = fields.String(default=None, allow_none=True, validate=[validate.Length(1,3000)])
    '''A brief description of the activity'''
    url = fields.String(default=None, allow_none=True, validate=[validate.Length(None,1000)])
    '''The API route/url that this activity belongs to'''
    good_bad = fields.Integer(default=3, allow_none=False, required=True, validate=[validate.OneOf([1, 2, 3, 4, 5])])
    '''A score from 1-5 for how good or bad this activity is.'''
    desirability = fields.Integer(default=3, allow_none=False, required=True, validate=[validate.OneOf([1, 2, 3, 4, 5])])
    '''A score from 1-5 of how desirable the activity is.'''
    extroversion = fields.Integer(default=3, allow_none=False, required=True,validate=[validate.OneOf([1, 2, 3, 4, 5])])
    '''A score from 1-5 for how extroverted the activity is.'''
    user_responsibility = fields.Integer(default=2, allow_none=False, required=True, validate=[validate.OneOf([1, 2, 3])])
    '''A score from 1-3 of how responsible the user is for the activity occuring.'''
    daily_limit = fields.Integer(default=None, allow_none=True, validate=[validate.Range(1,100000)])
    '''How many times per day the activity can be performed before requests are rejected. Defaults to null meaning infinite.'''
    probation_duration_days = fields.Integer(default=None, allow_none=True, validate=[validate.Range(1,365)])
    '''How many days the requestor will be prohibited from this activity, defaults to null.'''
    crud_type = CrudType(default=None, allow_none=True, validate=[validate.OneOf(['create', 'read', 'update', 'delete']), validate.Length(None,50)])
    '''The crud operation performed by this activity.'''
    is_deprecated = fields.Boolean(default=False, allow_none=False, required=True)
    '''1 if the activity should no longer be available for the api to find.'''
    is_primary = fields.Boolean(default=False, allow_none=False, required=True)
    '''1 if this activity is single successful'''
    is_live = fields.Boolean(default=True, allow_none=False, required=True)
    '''1 if this activity is ready to be executed through the api.'''
    is_error = fields.Boolean(default=False, allow_none=False, required=True)
    '''1 if this activity defines an error.'''

    def __repr__(self):
        return f"<{self.class_name}:>"





class ReadActivitiesSchema(BaseSchema):
    '''
        The ReadActivitiesSchema class


        Meta
        ----------
        `@author`: Colemen Atwood
        `@created`: 03-17-2023 10:09:46
        `@memberOf`: ActivitiesSchema
    '''
    class Meta:
        model = Activity
        include_relationships = True
        load_instance = True
        unknown=EXCLUDE

    hash_id = fields.String(default=None, allow_none=True, validate=[validate.Length(None,50)])
    '''The id used to externally identify this row.'''
    timestamp = fields.Integer(default=current_unix_timestamp(), allow_none=True, dump_only=True)
    '''The unix timestamp of when this was created.'''
    modified_timestamp = fields.Integer(default=None, allow_none=True, dump_only=True)
    '''The unix timestamp of when this was last modified, null otherwise.'''



    def __repr__(self):
        return f"<{self.class_name}:>"





class UpdateActivitiesSchema(BaseSchema):
    '''
        The UpdateActivitiesSchema class


        Meta
        ----------
        `@author`: Colemen Atwood
        `@created`: 03-17-2023 10:09:46
        `@memberOf`: ActivitiesSchema
    '''
    class Meta:
        model = Activity
        include_relationships = True
        load_instance = True
        unknown=EXCLUDE

    activity_id = HashidPrimary(required=True,allow_none=False)
    # hash_id = fields.String(allow_none=False, required=False, validate=[validate.Length(1,255)],dump_only=True)

    title = fields.String(allow_none=False, required=False, validate=[validate.Length(1,255)])
    '''The title of this activity'''
    description = fields.String(default=None, allow_none=True, validate=[validate.Length(1,3000)])
    '''A brief description of the activity'''
    url = fields.String(default=None, allow_none=True, validate=[validate.Length(None,1000)])
    '''The API route/url that this activity belongs to'''
    good_bad = fields.Integer(default=3, allow_none=False, required=False, validate=[validate.OneOf([1, 2, 3, 4, 5])])
    '''A score from 1-5 for how good or bad this activity is.'''
    desirability = fields.Integer(default=3, allow_none=False, required=False, validate=[validate.OneOf([1, 2, 3, 4, 5])])
    '''A score from 1-5 of how desirable the activity is.'''
    extroversion = fields.Integer(default=3, allow_none=False, required=False)
    '''A score from 1-5 for how extroverted the activity is.'''
    user_responsibility = fields.Integer(default=2, allow_none=False, required=False, validate=[validate.OneOf([1, 2, 3])])
    '''A score from 1-3 of how responsible the user is for the activity occuring.'''
    daily_limit = fields.Integer(default=None, allow_none=True, validate=[validate.Range(1,100000)])
    '''How many times per day the activity can be performed before requests are rejected. Defaults to null meaning infinite.'''
    probation_duration_days = fields.Integer(default=None, allow_none=True, validate=[validate.Range(1,365)])
    '''How many days the requestor will be prohibited from this activity, defaults to null.'''
    crud_type = CrudType(default=None, allow_none=True, validate=[validate.OneOf(['create', 'read', 'update', 'delete']), validate.Length(None,50)])
    '''The crud operation performed by this activity.'''
    is_deprecated = fields.Boolean(default=False, allow_none=False, required=False)
    '''1 if the activity should no longer be available for the api to find.'''
    is_primary = fields.Boolean(default=False, allow_none=False, required=False)
    '''1 if this activity is single successful'''
    is_live = fields.Boolean(default=True, allow_none=False, required=False)
    '''1 if this activity is ready to be executed through the api.'''
    is_error = fields.Boolean(default=False, allow_none=False, required=False)
    '''1 if this activity defines an error.'''
    deleted = fields.Integer(default=None, allow_none=True, dump_only=True)
    '''The unix timestamp of when this was deleted, null otherwise.'''



    def __repr__(self):
        return f"<{self.class_name}:>"


    def update(self, obj, data):
        """Update object nullifying missing data"""
        loadable_fields = [
            k for k, v in self.fields.items() if not v.dump_only
        ]
        for name in loadable_fields:
            setattr(obj, name, data.get(name))






class DeleteActivitiesSchema(BaseSchema):
    '''
        The DeleteActivitiesSchema class


        Meta
        ----------
        `@author`: Colemen Atwood
        `@created`: 03-17-2023 10:09:46
        `@memberOf`: ActivitiesSchema
    '''
    class Meta:
        model = Activity
        ordered = True
        #        include_fk = True
        unknown = EXCLUDE

    activity_id = HashidPrimary(required=True)
    '''The primary key of the table.'''



    def __repr__(self):
        return f"<{self.class_name}:>"





class PublicActivitiesSchema(BaseSchema):
    '''
        The PublicActivitiesSchema class


        Meta
        ----------
        `@author`: Colemen Atwood
        `@created`: 03-17-2023 10:09:46
        `@memberOf`: ActivitiesSchema
    '''
    class Meta:
        model = Activity
        include_relationships = True
        load_instance = True
        unknown=EXCLUDE

    activity_id = HashidPrimary()
    '''The primary key of the table.'''
    hash_id = fields.String(default=None, allow_none=True, validate=[validate.Length(None,50)])
    '''The id used to externally identify this row.'''
    title = fields.String(allow_none=False, required=True, validate=[validate.Length(1,255)])
    '''The title of this activity'''
    description = fields.String(default=None, allow_none=True, validate=[validate.Length(1,3000)])
    '''A brief description of the activity'''
    url = fields.String(default=None, allow_none=True, validate=[validate.Length(None,1000)])
    '''The API route/url that this activity belongs to'''
    good_bad = fields.Integer(default=3, allow_none=False, required=True, validate=[validate.OneOf([1, 2, 3, 4, 5])])
    '''A score from 1-5 for how good or bad this activity is.'''
    desirability = fields.Integer(default=3, allow_none=False, required=True, validate=[validate.OneOf([1, 2, 3, 4, 5])])
    '''A score from 1-5 of how desirable the activity is.'''
    extroversion = fields.Integer(default=3, allow_none=False, required=True)
    '''A score from 1-5 for how extroverted the activity is.'''
    user_responsibility = fields.Integer(default=2, allow_none=False, required=True, validate=[validate.OneOf([1, 2, 3])])
    '''A score from 1-3 of how responsible the user is for the activity occuring.'''
    daily_limit = fields.Integer(default=None, allow_none=True, validate=[validate.Range(1,100000)])
    '''How many times per day the activity can be performed before requests are rejected. Defaults to null meaning infinite.'''
    probation_duration_days = fields.Integer(default=None, allow_none=True, validate=[validate.Range(1,365)])
    '''How many days the requestor will be prohibited from this activity, defaults to null.'''
    crud_type = CrudType(default=None, allow_none=True, validate=[validate.OneOf(['create', 'read', 'update', 'delete']), validate.Length(None,50)])
    '''The crud operation performed by this activity.'''
    is_deprecated = fields.Boolean(default=False, allow_none=False, required=True)
    '''1 if the activity should no longer be available for the api to find.'''
    is_primary = fields.Boolean(default=False, allow_none=False, required=True)
    '''1 if this activity is single successful'''
    is_live = fields.Boolean(default=True, allow_none=False, required=True)
    '''1 if this activity is ready to be executed through the api.'''
    is_error = fields.Boolean(default=False, allow_none=False, required=True)
    '''1 if this activity defines an error.'''
    timestamp = fields.Integer(default=current_unix_timestamp(), allow_none=True, dump_only=True)
    '''The unix timestamp of when this was created.'''
    modified_timestamp = fields.Integer(default=None, allow_none=True, dump_only=True)
    '''The unix timestamp of when this was last modified, null otherwise.'''



    def __repr__(self):
        return f"<{self.class_name}:>"



