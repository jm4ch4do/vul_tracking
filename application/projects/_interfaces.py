import typing as _t
from abc import ABC, abstractmethod

import domain.project as _d_pro


class ProjectRepository(ABC):
    @abstractmethod
    def list_projects(self) -> _t.List[_d_pro.Project]:
        pass

    @abstractmethod
    def add_project(self) -> _t.List[_d_pro.Project]:
        pass
