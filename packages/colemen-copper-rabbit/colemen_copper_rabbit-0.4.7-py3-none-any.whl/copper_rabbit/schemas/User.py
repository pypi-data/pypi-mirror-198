# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import
'''
    The UsersSchema Schemas

    ----------

    Meta
    ----------
    `author`: Colemen Atwood
    `created`: 03-17-2023 08:42:59
    `memberOf`: schemas
    `name`: UsersSchema
'''


from __future__ import annotations
from typing import Iterable, List, Union

from marshmallow import Schema, fields, validate, ValidationError,EXCLUDE
import colemen_utils as c


# from copper_rabbit.settings.globe import base as _base
import copper_rabbit.settings as _settings
from copper_rabbit.models.User import User
from copper_rabbit.custom_fields import StatusCode,CrudType,RequestMethod,RequestLog,HashidPrimary,DeletedTimestamp
from copper_rabbit.support.BaseSchema import BaseSchema
from copper_rabbit.support.timestamp import current_unix_timestamp








class CreateUsersSchema(BaseSchema):
    '''
        The CreateUsersSchema class


        Meta
        ----------
        `@author`: Colemen Atwood
        `@created`: 03-17-2023 08:42:59
        `@memberOf`: UsersSchema
    '''
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        unknown=EXCLUDE

    first_name = fields.String(allow_none=False, required=True, validate=[validate.Length(None,255)])
    '''The users first name'''
    last_name = fields.String(allow_none=False, required=True, validate=[validate.Length(None,255)])
    '''The users last name'''
    email = fields.String(allow_none=False, required=True, validate=[validate.Length(None,100)])
    '''The users email address'''
    password = fields.String(allow_none=False, required=True, validate=[validate.Length(None,100)])
    '''The users password hashed with salt'''



    def __repr__(self):
        return f"<{self.class_name}:>"





class ReadUsersSchema(BaseSchema):
    '''
        The ReadUsersSchema class


        Meta
        ----------
        `@author`: Colemen Atwood
        `@created`: 03-17-2023 08:42:59
        `@memberOf`: UsersSchema
    '''
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        unknown=EXCLUDE
        include_fk = True

    hash_id = fields.String(default=None, allow_none=True, validate=[validate.Length(None,50)])
    '''The id used to externally identify this row.'''
    profile_name = fields.String(default=None, allow_none=True, validate=[validate.Length(None,500)])
    '''The profile name that is publicly visible.'''
    timestamp = fields.Integer(default=current_unix_timestamp(), allow_none=True, dump_only=True)
    '''The unix timestamp of when this was created.'''
    modified_timestamp = fields.Integer(default=None, allow_none=True, dump_only=True)
    '''The unix timestamp of when this was last modified, null otherwise.'''



    def __repr__(self):
        return f"<{self.class_name}:>"





class UpdateUsersSchema(BaseSchema):
    '''
        The UpdateUsersSchema class


        Meta
        ----------
        `@author`: Colemen Atwood
        `@created`: 03-17-2023 08:42:59
        `@memberOf`: UsersSchema
    '''
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        unknown=EXCLUDE
        include_fk = True

    first_name = fields.String(allow_none=False, required=True, validate=[validate.Length(None,255)])
    '''The users first name'''
    last_name = fields.String(allow_none=False, required=True, validate=[validate.Length(None,255)])
    '''The users last name'''
    email = fields.String(allow_none=False, required=True, validate=[validate.Length(None,100)])
    '''The users email address'''
    password = fields.String(allow_none=False, required=True, validate=[validate.Length(None,100)])
    '''The users password hashed with salt'''
    gender = fields.Integer(default=None, allow_none=True, validate=[validate.OneOf([0, 1, 2])])
    '''The users gender, 0-female, 1-male, 2-other'''
    birthday = fields.Integer(default=None, allow_none=True)
    '''The unix timestamp for the users birthday'''
    biography = fields.String(default=None, allow_none=True, validate=[validate.Length(None,500)])
    '''A brief biography about the user.'''
    is_public = fields.Boolean(default=True, allow_none=True)
    '''1 if the profile is publicly visible/searchable, 0 otherwise'''
    allow_followers = fields.Boolean(default=True, allow_none=True)
    '''1 if the user allows their profile to have followers'''
    is_messaging_public = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to allow anyone to message them.'''
    email_notifications = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants us to send them emails to alert them to new notifications.'''
    email_newsletters = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants us to send them periodic newsletters.'''
    send_new_device_emails = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants us to send them emails when a new device accesses their account.'''
    phone_number = fields.String(default=None, allow_none=True, validate=[validate.Length(None,45)])
    '''The users phone number that is used for authentication.'''
    send_job_emails = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to receive emails about jobs they might be interested in.'''
    send_job_notifications = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to receive notifications about jobs they might be interested in.'''
    theme = fields.String(default=None, allow_none=True, validate=[validate.OneOf(['dark', 'light']), validate.Length(None,45)])
    '''The name of theme the user wants the frontend to use.'''
    willing_to_relocate_career = fields.Boolean(default=False, allow_none=True)
    '''1 if the user is willing to relocate for a job.'''
    notif_comments = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to receive notification when their content receives a comment.'''
    notif_mentions = fields.Boolean(default=True, allow_none=True)
    '''1 if the user want to receive notifications when they are mentioned in comments or posts.'''
    notif_follows = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to be notified when they receive a new follower'''
    notif_following_activity = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to be notified when the subject they follow produces some content.'''
    send_social_emails = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to receive emails in conjunction with social notifications.'''
    vid_autoplay_desktop = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants videos to auto play on desktop devices.'''
    vid_autoplay_mobile = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants videos to autoplay on mobile devices.'''
    deactivated = fields.Integer(default=None, allow_none=True)
    '''The unix timestamp of when the user deactivated their account.'''
    disabled = fields.Integer(default=None, allow_none=True)
    '''The unix timestamp of when Equari disabled this users account.'''
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






class DeleteUsersSchema(BaseSchema):
    '''
        The DeleteUsersSchema class


        Meta
        ----------
        `@author`: Colemen Atwood
        `@created`: 03-17-2023 08:42:59
        `@memberOf`: UsersSchema
    '''
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        unknown=EXCLUDE
        include_fk = True

    user_id = HashidPrimary()
    '''The primary id of the table'''



    def __repr__(self):
        return f"<{self.class_name}:>"





class PublicUsersSchema(BaseSchema):
    '''
        The PublicUsersSchema class


        Meta
        ----------
        `@author`: Colemen Atwood
        `@created`: 03-17-2023 08:42:59
        `@memberOf`: UsersSchema
    '''
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        unknown=EXCLUDE
        include_fk = True

    user_id = HashidPrimary()
    '''The primary id of the table'''
    hash_id = fields.String(default=None, allow_none=True, validate=[validate.Length(None,50)])
    '''The id used to externally identify this row.'''
    stripe_customer_id = fields.String(default=None, allow_none=True, validate=[validate.Length(None,50)])
    '''The stripe customer id'''
    first_name = fields.String(allow_none=False, required=True, validate=[validate.Length(None,255)])
    '''The users first name'''
    last_name = fields.String(allow_none=False, required=True, validate=[validate.Length(None,255)])
    '''The users last name'''
    email = fields.String(allow_none=False, required=True, validate=[validate.Length(None,100)])
    '''The users email address'''
    gender = fields.Integer(default=None, allow_none=True, validate=[validate.OneOf([0, 1, 2])])
    '''The users gender, 0-female, 1-male, 2-other'''
    birthday = fields.Integer(default=None, allow_none=True)
    '''The unix timestamp for the users birthday'''
    last_login_timestamp = fields.Integer(default=None, allow_none=True)
    '''The unix timestamp of the last successful login'''
    profile_name = fields.String(default=None, allow_none=True, validate=[validate.Length(None,500)])
    '''The profile name that is publicly visible.'''
    profile_url = fields.String(default=None, allow_none=True, validate=[validate.Length(None,500)])
    '''The url/route to the users profile page.'''
    biography = fields.String(default=None, allow_none=True, validate=[validate.Length(None,500)])
    '''A brief biography about the user.'''
    is_public = fields.Boolean(default=True, allow_none=True)
    '''1 if the profile is publicly visible/searchable, 0 otherwise'''
    allow_followers = fields.Boolean(default=True, allow_none=True)
    '''1 if the user allows their profile to have followers'''
    is_messaging_public = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to allow anyone to message them.'''
    email_notifications = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants us to send them emails to alert them to new notifications.'''
    email_newsletters = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants us to send them periodic newsletters.'''
    send_new_device_emails = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants us to send them emails when a new device accesses their account.'''
    email_verified = fields.Integer(default=None, allow_none=True)
    '''The unix timestamp of when their email was successfully'''
    phone_number = fields.String(default=None, allow_none=True, validate=[validate.Length(None,45)])
    '''The users phone number that is used for authentication.'''
    send_job_emails = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to receive emails about jobs they might be interested in.'''
    send_job_notifications = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to receive notifications about jobs they might be interested in.'''
    theme = fields.String(default=None, allow_none=True, validate=[validate.OneOf(['dark', 'light']), validate.Length(None,45)])
    '''The name of theme the user wants the frontend to use.'''
    willing_to_relocate_career = fields.Boolean(default=False, allow_none=True)
    '''1 if the user is willing to relocate for a job.'''
    notif_comments = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to receive notification when their content receives a comment.'''
    notif_mentions = fields.Boolean(default=True, allow_none=True)
    '''1 if the user want to receive notifications when they are mentioned in comments or posts.'''
    notif_follows = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to be notified when they receive a new follower'''
    notif_following_activity = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to be notified when the subject they follow produces some content.'''
    send_social_emails = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants to receive emails in conjunction with social notifications.'''
    vid_autoplay_desktop = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants videos to auto play on desktop devices.'''
    vid_autoplay_mobile = fields.Boolean(default=True, allow_none=True)
    '''1 if the user wants videos to autoplay on mobile devices.'''
    deactivated = fields.Integer(default=None, allow_none=True)
    '''The unix timestamp of when the user deactivated their account.'''
    disabled = fields.Integer(default=None, allow_none=True)
    '''The unix timestamp of when Equari disabled this users account.'''
    timestamp = fields.Integer(default=current_unix_timestamp(), allow_none=True, dump_only=True)
    '''The unix timestamp of when this was created.'''
    modified_timestamp = fields.Integer(default=None, allow_none=True, dump_only=True)
    '''The unix timestamp of when this was last modified, null otherwise.'''
    last_activity_timestamp = fields.Integer(default=None, allow_none=True)
    '''The unix timestamp of the last time the user performed an activity.'''
    is_abandoned = fields.Integer(default=None, allow_none=True)
    '''The unix timestamp of when the account was considered abandoned.'''
    last_abandoned_alert = fields.Integer(default=None, allow_none=True)
    '''The unix timestamp of the last time we sent a "come back" email.'''



    def __repr__(self):
        return f"<{self.class_name}:>"



