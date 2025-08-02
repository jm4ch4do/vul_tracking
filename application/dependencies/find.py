import typing as _t

import domain.dependency as _d_dep
import providers.repository.dependencies as _p_dep


class GetDependencies:
    def __init__(self):
        self.repo = _p_dep.DependencyRepo()

    def __call__(self) -> _t.List[_d_dep.Dependency]:
        return self.repo.list_dependencies()
