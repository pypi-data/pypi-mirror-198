# type: ignore
# pylint: disable=syntax-error
'''
    The User class

    ----------

    Meta
    ----------
    `author`: Colemen Atwood
    `created`: 03-17-2023 10:09:45
    `memberOf`: models
    `name`: User
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

from sqlalchemy_utils.types.password import PasswordType
from sqlalchemy import Integer,Boolean,ForeignKey,String,Column,UniqueConstraint
from sqlalchemy.orm import Mapped,mapped_column,relationship
import colemen_utils as c


from copper_rabbit.settings.globe import base as _base
from copper_rabbit.support import format_timestamp,current_unix_timestamp
import copper_rabbit.settings as _settings








class User(_base):
    __bind_key__ = 'content_database'
    __tablename__ = "users"



    user_id = Column(Integer, autoincrement=True, primary_key=True, comment='The primary id of the table')
    '''The primary id of the table'''
    hash_id = Column(String(50), nullable=True, default=None, comment='The id used to externally identify this row.')
    '''The id used to externally identify this row.'''
    stripe_customer_id = Column(String(50), nullable=True, default=None, comment='The stripe customer id')
    '''The stripe customer id'''
    first_name = Column(String(255), comment='The users first name')
    '''The users first name'''
    last_name = Column(String(255), comment='The users last name')
    '''The users last name'''
    email = Column(String(100), comment='The users email address',unique=True)
    '''The users email address'''
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
    ), comment='The users password hashed with salt')
    # password = Column(String(100), comment='The users password hashed with salt')
    '''The users password hashed with salt'''
    gender = Column(Integer, nullable=True, default=None, comment='The users gender, 0-female, 1-male, 2-other')
    '''The users gender, 0-female, 1-male, 2-other'''
    birthday = Column(Integer, nullable=True, default=None, comment='The unix timestamp for the users birthday')
    '''The unix timestamp for the users birthday'''
    last_login_timestamp = Column(Integer, nullable=True, default=None, comment='The unix timestamp of the last successful login')
    '''The unix timestamp of the last successful login'''
    profile_name = Column(String(500), nullable=True, default=None, comment='The profile name that is publicly visible.')
    '''The profile name that is publicly visible.'''
    profile_url = Column(String(500), nullable=True, default=None, comment='The url/route to the users profile page.')
    '''The url/route to the users profile page.'''
    biography = Column(String(500), nullable=True, default=None, comment='A brief biography about the user.')
    '''A brief biography about the user.'''
    is_public = Column(Boolean, nullable=True, default=True, comment='1 if the profile is publicly visible/searchable, 0 otherwise')
    '''1 if the profile is publicly visible/searchable, 0 otherwise'''
    allow_followers = Column(Boolean, nullable=True, default=True, comment='1 if the user allows their profile to have followers')
    '''1 if the user allows their profile to have followers'''
    is_messaging_public = Column(Boolean, nullable=True, default=True, comment='1 if the user wants to allow anyone to message them.')
    '''1 if the user wants to allow anyone to message them.'''
    email_notifications = Column(Boolean, nullable=True, default=True, comment='1 if the user wants us to send them emails to alert them to new notifications.')
    '''1 if the user wants us to send them emails to alert them to new notifications.'''
    email_newsletters = Column(Boolean, nullable=True, default=True, comment='1 if the user wants us to send them periodic newsletters.')
    '''1 if the user wants us to send them periodic newsletters.'''
    send_new_device_emails = Column(Boolean, nullable=True, default=True, comment='1 if the user wants us to send them emails when a new device accesses their account.')
    '''1 if the user wants us to send them emails when a new device accesses their account.'''
    email_verified = Column(Integer, nullable=True, default=None, comment='The unix timestamp of when their email was successfully')
    '''The unix timestamp of when their email was successfully'''
    phone_number = Column(String(45), nullable=True, default=None, comment='The users phone number that is used for authentication.')
    '''The users phone number that is used for authentication.'''
    send_job_emails = Column(Boolean, nullable=True, default=True, comment='1 if the user wants to receive emails about jobs they might be interested in.')
    '''1 if the user wants to receive emails about jobs they might be interested in.'''
    send_job_notifications = Column(Boolean, nullable=True, default=True, comment='1 if the user wants to receive notifications about jobs they might be interested in.')
    '''1 if the user wants to receive notifications about jobs they might be interested in.'''
    theme = Column(String(45), nullable=True, default=None, comment='The name of theme the user wants the frontend to use.')
    '''The name of theme the user wants the frontend to use.'''
    willing_to_relocate_career = Column(Boolean, nullable=True, default=False, comment='1 if the user is willing to relocate for a job.')
    '''1 if the user is willing to relocate for a job.'''
    notif_comments = Column(Boolean, nullable=True, default=True, comment='1 if the user wants to receive notification when their content receives a comment.')
    '''1 if the user wants to receive notification when their content receives a comment.'''
    notif_mentions = Column(Boolean, nullable=True, default=True, comment='1 if the user want to receive notifications when they are mentioned in comments or posts.')
    '''1 if the user want to receive notifications when they are mentioned in comments or posts.'''
    notif_follows = Column(Boolean, nullable=True, default=True, comment='1 if the user wants to be notified when they receive a new follower')
    '''1 if the user wants to be notified when they receive a new follower'''
    notif_following_activity = Column(Boolean, nullable=True, default=True, comment='1 if the user wants to be notified when the subject they follow produces some content.')
    '''1 if the user wants to be notified when the subject they follow produces some content.'''
    send_social_emails = Column(Boolean, nullable=True, default=True, comment='1 if the user wants to receive emails in conjunction with social notifications.')
    '''1 if the user wants to receive emails in conjunction with social notifications.'''
    vid_autoplay_desktop = Column(Boolean, nullable=True, default=True, comment='1 if the user wants videos to auto play on desktop devices.')
    '''1 if the user wants videos to auto play on desktop devices.'''
    vid_autoplay_mobile = Column(Boolean, nullable=True, default=True, comment='1 if the user wants videos to autoplay on mobile devices.')
    '''1 if the user wants videos to autoplay on mobile devices.'''
    deactivated = Column(Integer, nullable=True, default=None, comment='The unix timestamp of when the user deactivated their account.')
    '''The unix timestamp of when the user deactivated their account.'''
    disabled = Column(Integer, nullable=True, default=None, comment='The unix timestamp of when Equari disabled this users account.')
    '''The unix timestamp of when Equari disabled this users account.'''
    deleted = Column(Integer, nullable=True, default=None, comment='The unix timestamp of when this was deleted, null otherwise.')
    '''The unix timestamp of when this was deleted, null otherwise.'''
    timestamp = Column(Integer, nullable=True, default=current_unix_timestamp(), comment='The unix timestamp of when this was created.')
    '''The unix timestamp of when this was created.'''
    modified_timestamp = Column(Integer, nullable=True, default=None, onupdate=current_unix_timestamp(), comment='The unix timestamp of when this was last modified, null otherwise.')
    '''The unix timestamp of when this was last modified, null otherwise.'''
    last_activity_timestamp = Column(Integer, nullable=True, default=current_unix_timestamp(), onupdate=current_unix_timestamp(), comment='The unix timestamp of the last time the user performed an activity.')
    '''The unix timestamp of the last time the user performed an activity.'''
    is_abandoned = Column(Integer, nullable=True, default=None, comment='The unix timestamp of when the account was considered abandoned.')
    '''The unix timestamp of when the account was considered abandoned.'''
    last_abandoned_alert = Column(Integer, nullable=True, default=None, comment='The unix timestamp of the last time we sent a "come back" email.')
    '''The unix timestamp of the last time we sent a "come back" email.'''


    UniqueConstraint('email', name='unique_users_emailaddress_q7o0b5nykvq_l') # Ensure that the email column is unique.
    UniqueConstraint('hash_id', name='unique_users_hashid_es04rff_nx8n1') # Unique Constraint to ensure the event cannot have multiple addresses with the same title.


    # addresses: Mapped[List['Address']] = relationship()
    # animal_caretakers: Mapped[List['AnimalCaretaker']] = relationship()
    # animal_followers: Mapped[List['AnimalFollower']] = relationship()
    # animal_owners: Mapped[List['AnimalOwner']] = relationship()
    # animal_trusts: Mapped[List['AnimalTrust']] = relationship()
    # animals: Mapped[List['Animal']] = relationship()
    # barn_blocks: Mapped[List['BarnBlock']] = relationship()
    # barn_employees: Mapped[List['BarnEmployee']] = relationship()
    # barn_followers: Mapped[List['BarnFollower']] = relationship()
    # barn_owners: Mapped[List['BarnOwner']] = relationship()
    # barn_trusts: Mapped[List['BarnTrust']] = relationship()
    # comment_mentions: Mapped[List['CommentMention']] = relationship()
    # comments: Mapped[List['Comment']] = relationship()
    # education_histories: Mapped[List['EducationHistory']] = relationship()
    # events: Mapped[List['Event']] = relationship()
    # files: Mapped[List['File']] = relationship()
    # group_blocks: Mapped[List['GroupBlock']] = relationship()
    # groups: Mapped[List['Group']] = relationship()
    # inventories: Mapped[List['Inventory']] = relationship()
    # invitations: Mapped[List['Invitation']] = relationship()
    # notifications: Mapped[List['Notification']] = relationship()
    # posts: Mapped[List['Post']] = relationship()
    # reviews: Mapped[List['Review']] = relationship()
    # service_requests: Mapped[List['ServiceRequest']] = relationship()
    # sessions: Mapped[List['Session']] = relationship()
    # suggestions: Mapped[List['Suggestion']] = relationship()
    # support_notes: Mapped[List['SupportNote']] = relationship()
    # support_requests: Mapped[List['SupportRequest']] = relationship()
    # task_lists: Mapped[List['TaskList']] = relationship()
    # tasks: Mapped[List['Task']] = relationship()
    tokens: Mapped[List['Token']] = relationship()
    # user_blocks: Mapped[List['UserBlock']] = relationship()
    # user_devices: Mapped[List['UserDevice']] = relationship()
    # user_follows: Mapped[List['UserFollow']] = relationship()
    # user_groups: Mapped[List['UserGroup']] = relationship()
    # user_roles: Mapped[List['UserRole']] = relationship()
    # wish_lists: Mapped[List['WishList']] = relationship()
    # work_histories: Mapped[List['WorkHistory']] = relationship()




    def __init__(
        self,
        user_id:int=None,
        hash_id:str=None,
        stripe_customer_id:str=None,
        first_name:str=None,
        last_name:str=None,
        email:str=None,
        password:str=None,
        gender:int=None,
        birthday:int=None,
        last_login_timestamp:int=None,
        profile_name:str=None,
        profile_url:str=None,
        biography:str=None,
        is_public:bool=True,
        allow_followers:bool=True,
        is_messaging_public:bool=True,
        email_notifications:bool=True,
        email_newsletters:bool=True,
        send_new_device_emails:bool=True,
        email_verified:int=None,
        phone_number:str=None,
        send_job_emails:bool=True,
        send_job_notifications:bool=True,
        theme:str=None,
        willing_to_relocate_career:bool=False,
        notif_comments:bool=True,
        notif_mentions:bool=True,
        notif_follows:bool=True,
        notif_following_activity:bool=True,
        send_social_emails:bool=True,
        vid_autoplay_desktop:bool=True,
        vid_autoplay_mobile:bool=True,
        deactivated:int=None,
        disabled:int=None,
        deleted:int=None,
        timestamp:int=None,
        modified_timestamp:int=None,
        last_activity_timestamp:int=None,
        is_abandoned:int=None,
        last_abandoned_alert:int=None
        ):

        self.user_id = user_id
        self.hash_id = hash_id
        self.stripe_customer_id = stripe_customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.gender = gender
        self.birthday = birthday
        self.last_login_timestamp = last_login_timestamp
        self.profile_name = profile_name
        self.profile_url = profile_url
        self.biography = biography
        self.is_public = is_public
        self.allow_followers = allow_followers
        self.is_messaging_public = is_messaging_public
        self.email_notifications = email_notifications
        self.email_newsletters = email_newsletters
        self.send_new_device_emails = send_new_device_emails
        self.email_verified = email_verified
        self.phone_number = phone_number
        self.send_job_emails = send_job_emails
        self.send_job_notifications = send_job_notifications
        self.theme = theme
        self.willing_to_relocate_career = willing_to_relocate_career
        self.notif_comments = notif_comments
        self.notif_mentions = notif_mentions
        self.notif_follows = notif_follows
        self.notif_following_activity = notif_following_activity
        self.send_social_emails = send_social_emails
        self.vid_autoplay_desktop = vid_autoplay_desktop
        self.vid_autoplay_mobile = vid_autoplay_mobile
        self.deactivated = deactivated
        self.disabled = disabled
        self.deleted = deleted
        self.timestamp = timestamp
        self.modified_timestamp = modified_timestamp
        self.last_activity_timestamp = last_activity_timestamp
        self.is_abandoned = is_abandoned
        self.last_abandoned_alert = last_abandoned_alert



    def save(self):
        '''
            Save (submit or update) this User model to the database
            ----------

            Return {type}
            ----------------------
            return_description

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 03-17-2023 10:09:45
            `memberOf`: User
            `version`: 1.0
            `method_name`: save
            * @xxx [03-17-2023 10:09:45]: documentation for save
        '''
        _settings.globe.session.add(self)
        _settings.globe.session.commit()

    def delete(self):
        '''
            Delete this User model from the database.
            ----------

            Return {type}
            ----------------------
            return_description

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 03-17-2023 10:09:45
            `memberOf`: User
            `version`: 1.0
            `method_name`: delete
            * @xxx [03-17-2023 10:09:45]: documentation for delete
        '''
        if self.user_id is not None:
            _settings.globe.session.delete(self)
            _settings.globe.session.commit()

    def soft_delete(self):
        '''
            Soft delete this User model in the database.
            ----------

            Return {type}
            ----------------------
            return_description

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 03-17-2023 10:09:45
            `memberOf`: User
            `version`: 1.0
            `method_name`: soft_delete
            * @xxx [03-17-2023 10:09:45]: documentation for soft_delete
        '''
        if self.user_id is not None:
            self.deleted = current_unix_timestamp()
            _settings.globe.session.add(self)
            _settings.globe.session.commit()


    def __repr__(self) -> str:
        return f"<UserModel:{self.user_id}>"
