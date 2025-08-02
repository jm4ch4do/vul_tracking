import typing as _t

import domain.dependency as _d_dep
import providers.repository.dependencies as _p_dep


class AddDependency:
    def __init__(self, repo: _p_dep.DependencyRepo = _p_dep.DependencyRepo()):
        self.repo = repo

    def __call__(self, dependency: _d_dep.Dependency) -> None:
        self.repo.add_dependency(dependency)
