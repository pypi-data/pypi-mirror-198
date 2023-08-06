# type: ignore
# pylint: disable=syntax-error
'''
    The Activity class

    ----------

    Meta
    ----------
    `author`: Colemen Atwood
    `created`: 03-17-2023 10:09:45
    `memberOf`: models
    `name`: Activity
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import


from __future__ import annotations
from datetime import datetime
from datetime import timezone
from typing import Iterable, List, Union
import re


from sqlalchemy import Integer,Boolean,ForeignKey,String,Column,UniqueConstraint
from sqlalchemy.orm import Mapped,mapped_column,relationship
import colemen_utils as c


from copper_rabbit.settings.globe import base as _base
from copper_rabbit.support import format_timestamp,current_unix_timestamp
import copper_rabbit.settings as _settings








class Activity(_base):
    __bind_key__ = 'management_database'
    __tablename__ = "activities"



    activity_id = Column(Integer, autoincrement=True, primary_key=True, comment='The primary key of the table.')
    '''The primary key of the table.'''
    hash_id = Column(String(50), nullable=True, default=None, comment='The id used to externally identify this row.')
    '''The id used to externally identify this row.'''
    title = Column(String(255), comment='The title of this activity')
    '''The title of this activity'''
    description = Column(String(3000), nullable=True, default=None, comment='A brief description of the activity')
    '''A brief description of the activity'''
    url = Column(String(1000), nullable=True, default=None, comment='The API route/url that this activity belongs to')
    '''The API route/url that this activity belongs to'''
    good_bad = Column(Integer, default=3, comment='A score from 1-5 for how good or bad this activity is.')
    '''A score from 1-5 for how good or bad this activity is.'''
    desirability = Column(Integer, default=3, comment='A score from 1-5 of how desirable the activity is.')
    '''A score from 1-5 of how desirable the activity is.'''
    extroversion = Column(Integer, default=3, comment='A score from 1-5 for how extroverted the activity is.')
    '''A score from 1-5 for how extroverted the activity is.'''
    user_responsibility = Column(Integer, default=2, comment='A score from 1-3 of how responsible the user is for the activity occuring.')
    '''A score from 1-3 of how responsible the user is for the activity occuring.'''
    daily_limit = Column(Integer, nullable=True, default=None, comment='How many times per day the activity can be performed before requests are rejected. Defaults to null meaning infinite.')
    '''How many times per day the activity can be performed before requests are rejected. Defaults to null meaning infinite.'''
    probation_duration_days = Column(Integer, nullable=True, default=None, comment='How many days the requestor will be prohibited from this activity, defaults to null.')
    '''How many days the requestor will be prohibited from this activity, defaults to null.'''
    crud_type = Column(String(50), nullable=True, default=None, comment='The crud operation performed by this activity.')
    '''The crud operation performed by this activity.'''
    is_deprecated = Column(Boolean, default=False, comment='1 if the activity should no longer be available for the api to find.')
    '''1 if the activity should no longer be available for the api to find.'''
    is_primary = Column(Boolean, default=False, comment='1 if this activity is single successful')
    '''1 if this activity is single successful'''
    is_live = Column(Boolean, default=True, comment='1 if this activity is ready to be executed through the api.')
    '''1 if this activity is ready to be executed through the api.'''
    is_error = Column(Boolean, default=False, comment='1 if this activity defines an error.')
    '''1 if this activity defines an error.'''
    timestamp = Column(Integer, nullable=True, default=current_unix_timestamp(), comment='The unix timestamp of when this was created.')
    '''The unix timestamp of when this was created.'''
    deleted = Column(Integer, nullable=True, default=None, comment='The unix timestamp of when this was deleted, null otherwise.')
    '''The unix timestamp of when this was deleted, null otherwise.'''
    modified_timestamp = Column(Integer, nullable=True, default=None, onupdate=current_unix_timestamp(), comment='The unix timestamp of when this was last modified, null otherwise.')
    '''The unix timestamp of when this was last modified, null otherwise.'''


    UniqueConstraint('hash_id', name='unique_activities_hashid') # Ensure that the hash_id column is unique.


    # activity_logs: Mapped[List['ActivityLog']] = relationship()
    # activity_public_responses: Mapped[List['ActivityPublicResponse']] = relationship()
    # role_activities: Mapped[List['RoleActivity']] = relationship()




    def __init__(
        self,
        activity_id:int=None,
        hash_id:str=None,
        title:str=None,
        description:str=None,
        url:str=None,
        good_bad:int=None,
        desirability:int=None,
        extroversion:int=None,
        user_responsibility:int=None,
        daily_limit:int=None,
        probation_duration_days:int=None,
        crud_type:str=None,
        is_deprecated:bool=False,
        is_primary:bool=False,
        is_live:bool=True,
        is_error:bool=False,
        timestamp:int=None,
        deleted:int=None,
        modified_timestamp:int=None
        ):

        self.activity_id = activity_id
        self.hash_id = hash_id
        self.title = title
        self.description = description
        self.url = url
        self.good_bad = good_bad
        self.desirability = desirability
        self.extroversion = extroversion
        self.user_responsibility = user_responsibility
        self.daily_limit = daily_limit
        self.probation_duration_days = probation_duration_days
        self.crud_type = crud_type
        self.is_deprecated = is_deprecated
        self.is_primary = is_primary
        self.is_live = is_live
        self.is_error = is_error
        self.timestamp = timestamp
        self.deleted = deleted
        self.modified_timestamp = modified_timestamp



    def save(self):
        '''
            Save (submit or update) this Activity model to the database
            ----------

            Return {type}
            ----------------------
            return_description

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 03-17-2023 10:09:45
            `memberOf`: Activity
            `version`: 1.0
            `method_name`: save
            * @xxx [03-17-2023 10:09:45]: documentation for save
        '''
        _settings.globe.session.add(self)
        _settings.globe.session.commit()

    def delete(self):
        '''
            Delete this Activity model from the database.
            ----------

            Return {type}
            ----------------------
            return_description

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 03-17-2023 10:09:45
            `memberOf`: Activity
            `version`: 1.0
            `method_name`: delete
            * @xxx [03-17-2023 10:09:45]: documentation for delete
        '''
        if self.activity_id is not None:
            _settings.globe.session.delete(self)
            _settings.globe.session.commit()

    def soft_delete(self):
        '''
            Soft delete this Activity model in the database.
            ----------

            Return {type}
            ----------------------
            return_description

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 03-17-2023 10:09:45
            `memberOf`: Activity
            `version`: 1.0
            `method_name`: soft_delete
            * @xxx [03-17-2023 10:09:45]: documentation for soft_delete
        '''
        if self.activity_id is not None:
            self.deleted = current_unix_timestamp()
            _settings.globe.session.add(self)
            _settings.globe.session.commit()



