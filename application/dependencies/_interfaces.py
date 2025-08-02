import typing as _t
from abc import ABC, abstractmethod

import domain.dependency as _d_dep


class DependencyRepository(ABC):
    @abstractmethod
    def list_dependencies(self) -> _t.List[_d_dep.Dependency]:
        pass

    @abstractmethod
    def add_dependency(self) -> _t.List[_d_dep.Dependency]:
        pass
