from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Union

from github.Commit import Commit
from github.File import File
from github.GithubObject import CompletableGithubObject, _NotSetType
from github.Issue import Issue
from github.IssueComment import IssueComment
from github.IssueEvent import IssueEvent
from github.Label import Label
from github.Milestone import Milestone
from github.NamedUser import NamedUser
from github.PaginatedList import PaginatedList
from github.PullRequestComment import PullRequestComment
from github.PullRequestMergeStatus import PullRequestMergeStatus
from github.PullRequestPart import PullRequestPart
from github.PullRequestReview import PullRequestReview
from github.Team import Team

class PullRequest(CompletableGithubObject):
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    def add_to_labels(self, *labels: Union[Label, str]) -> None: ...
    def add_to_assignees(self, *assignees: Union[NamedUser, str]) -> None: ...
    @property
    def additions(self) -> int: ...
    def as_issue(self) -> Issue: ...
    @property
    def assignee(self) -> NamedUser: ...
    @property
    def assignees(self) -> List[NamedUser]: ...
    @property
    def requested_reviewers(self) -> List[NamedUser]: ...
    @property
    def requested_teams(self) -> List[Team]: ...
    @property
    def base(self) -> PullRequestPart: ...
    @property
    def body(self) -> str: ...
    @property
    def changed_files(self) -> int: ...
    @property
    def closed_at(self) -> Optional[datetime]: ...
    @property
    def comments(self) -> int: ...
    @property
    def comments_url(self) -> str: ...
    @property
    def commits(self) -> int: ...
    @property
    def commits_url(self) -> str: ...
    def create_comment(
        self, body: str, commit_id: Commit, path: str, position: int
    ) -> PullRequestComment: ...
    def create_issue_comment(self, body: str) -> IssueComment: ...
    def create_review(
        self,
        commit: Commit = ...,
        body: Union[_NotSetType, str] = ...,
        event: Union[_NotSetType, str] = ...,
        comments: Union[_NotSetType, str] = ...,
    ) -> PullRequestReview: ...
    def create_review_comment(
        self, body: str, commit_id: Commit, path: str, position: int
    ) -> PullRequestComment: ...
    def create_review_request(
        self,
        reviewers: Union[_NotSetType, List[str]] = ...,
        team_reviewers: Union[_NotSetType, List[str]] = ...,
    ) -> None: ...
    @property
    def created_at(self) -> datetime: ...
    def delete_labels(self) -> None: ...
    def delete_review_request(
        self,
        reviewers: Union[_NotSetType, List[str]] = ...,
        team_reviewers: Union[_NotSetType, List[str]] = ...,
    ) -> None: ...
    @property
    def deletions(self) -> int: ...
    @property
    def diff_url(self) -> str: ...
    @property
    def draft(self) -> bool: ...
    def edit(
        self,
        title: Union[str, _NotSetType] = ...,
        body: Union[str, _NotSetType] = ...,
        state: Union[str, _NotSetType] = ...,
        base: Union[_NotSetType, str] = ...,
    ) -> None: ...
    def get_comment(self, id: int) -> PullRequestComment: ...
    def get_comments(self) -> PaginatedList[PullRequestComment]: ...
    def get_commits(self) -> PaginatedList[Commit]: ...
    def get_files(self) -> PaginatedList[File]: ...
    def get_issue_comment(self, id: int) -> IssueComment: ...
    def get_issue_comments(self) -> PaginatedList[IssueComment]: ...
    def get_issue_events(self) -> PaginatedList[IssueEvent]: ...
    def get_labels(self) -> PaginatedList[Label]: ...
    def get_review(self, id: int) -> PullRequestReview: ...
    def get_review_comment(self, id: int) -> PullRequestComment: ...
    def get_review_comments(
        self, since: Union[_NotSetType, datetime] = ...
    ) -> PaginatedList[PullRequestComment]: ...
    def get_single_review_comments(
        self, id: int
    ) -> PaginatedList[PullRequestComment]: ...
    def get_review_requests(
        self,
    ) -> Tuple[PaginatedList[NamedUser], PaginatedList[Team]]: ...
    def get_reviews(self) -> PaginatedList[PullRequestReview]: ...
    @property
    def head(self) -> PullRequestPart: ...
    @property
    def html_url(self) -> str: ...
    @property
    def id(self) -> int: ...
    def is_merged(self) -> bool: ...
    @property
    def issue_url(self) -> str: ...
    @property
    def labels(self) -> List[Label]: ...
    @property
    def maintainer_can_modify(self) -> bool: ...
    def merge(
        self,
        commit_message: Union[str, _NotSetType] = ...,
        commit_title: Union[str, _NotSetType] = ...,
        merge_method: Union[str, _NotSetType] = ...,
        sha: Union[str, _NotSetType] = ...,
    ) -> PullRequestMergeStatus: ...
    @property
    def merge_commit_sha(self) -> str: ...
    @property
    def mergeable(self) -> Optional[bool]: ...
    @property
    def mergeable_state(self) -> str: ...
    @property
    def merged(self) -> bool: ...
    @property
    def merged_at(self) -> datetime: ...
    @property
    def merged_by(self) -> NamedUser: ...
    @property
    def milestone(self) -> Milestone: ...
    @property
    def number(self) -> int: ...
    @property
    def patch_url(self) -> str: ...
    @property
    def rebaseable(self) -> bool: ...
    def remove_from_labels(self, label: Union[Label, str]) -> None: ...
    @property
    def review_comment_url(self) -> str: ...
    @property
    def review_comments(self) -> int: ...
    @property
    def review_comments_url(self) -> str: ...
    def set_labels(self, *labels: Union[Label, str]) -> None: ...
    @property
    def state(self) -> str: ...
    @property
    def title(self) -> str: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
    @property
    def user(self) -> NamedUser: ...
