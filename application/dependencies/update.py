import typing as _t

import domain.dependency as _d_dep
import providers.repository.dependencies as _p_dep


class ToogleVulsInDependencies:
    def __init__(self):
        self.repo = _p_dep.DependencyRepo()

    def __call__(self, dep_ids: _t.Tuple[str]) -> None:
        self.repo.toggle_vulnerability(dep_ids)
