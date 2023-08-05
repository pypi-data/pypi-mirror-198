from datetime import datetime
from typing import Any, Dict, List, Optional, Union, NamedTuple

from github.Authorization import Authorization
from github.Event import Event
from github.Gist import Gist
from github.GithubObject import CompletableGithubObject, _NotSetType
from github.InputFileContent import InputFileContent
from github.Invitation import Invitation
from github.Issue import Issue
from github.Label import Label
from github.Membership import Membership
from github.Migration import Migration
from github.NamedUser import NamedUser
from github.Notification import Notification
from github.Organization import Organization
from github.PaginatedList import PaginatedList
from github.Plan import Plan
from github.Repository import Repository
from github.Team import Team
from github.UserKey import UserKey

class EmailData(NamedTuple):
    email: str
    primary: bool
    verified: bool
    visibility: str

class AuthenticatedUser(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    def accept_invitation(self, invitation: Union[int, Invitation]) -> None: ...
    def add_to_emails(self, *emails: List[str]) -> None: ...
    def add_to_following(self, following: NamedUser) -> None: ...
    def add_to_starred(self, starred: Repository) -> None: ...
    def add_to_subscriptions(self, subscription: Repository) -> None: ...
    def add_to_watched(self, watched: Repository) -> None: ...
    @property
    def avatar_url(self) -> str: ...
    @property
    def bio(self) -> str: ...
    @property
    def blog(self) -> str: ...
    @property
    def collaborators(self) -> int: ...
    @property
    def company(self) -> str: ...
    def create_authorization(
        self,
        scopes: Union[List[str], _NotSetType] = ...,
        note: Union[str, _NotSetType] = ...,
        note_url: Union[str, _NotSetType] = ...,
        client_id: Union[str, _NotSetType] = ...,
        client_secret: Union[str, _NotSetType] = ...,
        onetime_password: Union[str, None] = ...,
    ) -> Authorization: ...
    def create_fork(self, repo: Repository) -> Repository: ...
    def create_gist(
        self,
        public: bool,
        files: Dict[str, InputFileContent],
        description: Union[str, _NotSetType] = ...,
    ) -> Gist: ...
    def create_key(self, title: str, key: str) -> UserKey: ...
    def create_migration(
        self,
        repos: List[str],
        lock_repositories: Union[bool, _NotSetType] = ...,
        exclude_attachments: Union[bool, _NotSetType] = ...,
    ) -> Migration: ...
    def create_repo(
        self,
        name: str,
        description: Union[str, _NotSetType] = ...,
        homepage: Union[str, _NotSetType] = ...,
        private: Union[bool, _NotSetType] = ...,
        has_issues: Union[bool, _NotSetType] = ...,
        has_wiki: Union[bool, _NotSetType] = ...,
        has_downloads: Union[bool, _NotSetType] = ...,
        has_projects: Union[bool, _NotSetType] = ...,
        auto_init: Union[bool, _NotSetType] = ...,
        license_template: _NotSetType = ...,
        gitignore_template: Union[str, _NotSetType] = ...,
        allow_squash_merge: Union[bool, _NotSetType] = ...,
        allow_merge_commit: Union[bool, _NotSetType] = ...,
        allow_rebase_merge: Union[bool, _NotSetType] = ...,
    ) -> Repository: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def disk_usage(self) -> int: ...
    def edit(
        self,
        name: Union[str, _NotSetType] = ...,
        email: Union[str, _NotSetType] = ...,
        blog: Union[str, _NotSetType] = ...,
        company: Union[str, _NotSetType] = ...,
        location: Union[str, _NotSetType] = ...,
        hireable: Union[bool, _NotSetType] = ...,
        bio: Union[str, _NotSetType] = ...,
    ) -> None: ...
    @property
    def email(self) -> str: ...
    @property
    def events_url(self) -> str: ...
    @property
    def followers(self) -> int: ...
    @property
    def followers_url(self) -> str: ...
    @property
    def following(self) -> int: ...
    @property
    def following_url(self) -> str: ...
    def get_authorization(self, id: int) -> Authorization: ...
    def get_authorizations(self) -> PaginatedList[Authorization]: ...
    def get_emails(self) -> List[EmailData]: ...
    def get_events(self) -> PaginatedList[Event]: ...
    def get_followers(self) -> PaginatedList[NamedUser]: ...
    def get_following(self) -> PaginatedList[NamedUser]: ...
    def get_gists(
        self, since: Union[datetime, _NotSetType] = ...
    ) -> PaginatedList[Gist]: ...
    def get_invitations(self) -> PaginatedList[Invitation]: ...
    def get_issues(
        self,
        filter: Union[str, _NotSetType] = ...,
        state: Union[str, _NotSetType] = ...,
        labels: Union[List[Label], _NotSetType] = ...,
        sort: Union[str, _NotSetType] = ...,
        direction: Union[str, _NotSetType] = ...,
        since: Union[_NotSetType, datetime] = ...,
    ) -> PaginatedList[Issue]: ...
    def get_key(self, id: int) -> UserKey: ...
    def get_keys(self) -> PaginatedList[UserKey]: ...
    def get_migrations(self) -> PaginatedList[Migration]: ...
    def get_notification(self, id: str) -> Notification: ...
    def get_notifications(
        self,
        all: Union[bool, _NotSetType] = ...,
        participating: Union[bool, _NotSetType] = ...,
        since: Union[datetime, _NotSetType] = ...,
        before: Union[datetime, _NotSetType] = ...,
    ) -> PaginatedList[Notification]: ...
    def get_organization_events(self, org: Organization) -> PaginatedList[Event]: ...
    def get_organization_membership(self, org: int) -> Membership: ...
    def get_orgs(self) -> PaginatedList[Organization]: ...
    def get_repo(self, name: str) -> Repository: ...
    def get_repos(
        self,
        visibility: Union[str, _NotSetType] = ...,
        affiliation: Union[str, _NotSetType] = ...,
        type: Union[str, _NotSetType] = ...,
        sort: Union[str, _NotSetType] = ...,
        direction: Union[str, _NotSetType] = ...,
    ) -> PaginatedList[Repository]: ...
    def get_starred(self) -> PaginatedList[Repository]: ...
    def get_starred_gists(self) -> PaginatedList[Gist]: ...
    def get_subscriptions(self) -> PaginatedList[Repository]: ...
    def get_teams(self) -> PaginatedList[Team]: ...
    def get_user_issues(
        self,
        filter: Union[str, _NotSetType] = ...,
        state: Union[str, _NotSetType] = ...,
        labels: Union[List[Label], _NotSetType] = ...,
        sort: Union[str, _NotSetType] = ...,
        direction: Union[str, _NotSetType] = ...,
        since: Union[_NotSetType, datetime] = ...,
    ) -> PaginatedList[Issue]: ...
    def get_watched(self) -> PaginatedList[Repository]: ...
    @property
    def gists_url(self) -> str: ...
    @property
    def gravatar_id(self) -> str: ...
    def has_in_following(self, following: NamedUser) -> bool: ...
    def has_in_starred(self, starred: Repository) -> bool: ...
    def has_in_subscriptions(self, subscription: Repository) -> bool: ...
    def has_in_watched(self, watched: Repository) -> bool: ...
    @property
    def hireable(self) -> bool: ...
    @property
    def html_url(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def location(self) -> str: ...
    @property
    def login(self) -> str: ...
    def mark_notifications_as_read(self, last_read_at: datetime = ...) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def node_id(self) -> str: ...
    @property
    def organizations_url(self) -> str: ...
    @property
    def owned_private_repos(self) -> int: ...
    @property
    def plan(self) -> Plan: ...
    @property
    def private_gists(self) -> int: ...
    @property
    def public_gists(self) -> int: ...
    @property
    def public_repos(self) -> int: ...
    @property
    def received_events_url(self) -> str: ...
    def remove_from_emails(self, *emails: str) -> None: ...
    def remove_from_following(self, following: NamedUser) -> None: ...
    def remove_from_starred(self, starred: Repository) -> None: ...
    def remove_from_subscriptions(self, subscription: Repository) -> None: ...
    def remove_from_watched(self, watched: Repository) -> None: ...
    @property
    def repos_url(self) -> str: ...
    @property
    def site_admin(self) -> bool: ...
    @property
    def starred_url(self) -> str: ...
    @property
    def subscriptions_url(self) -> str: ...
    @property
    def total_private_repos(self) -> int: ...
    @property
    def type(self) -> str: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
    @property
    def two_factor_authentication(self) -> bool: ...
