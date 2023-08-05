from typing import Any, Dict

from github.GithubObject import NonCompletableGithubObject

class CheckRunOutput(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def annotations_count(self) -> int: ...
    @property
    def annotations_url(self) -> str: ...
    @property
    def summary(self) -> str: ...
    @property
    def text(self) -> str: ...
    @property
    def title(self) -> str: ...
