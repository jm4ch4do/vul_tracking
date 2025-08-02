import typing as _t

import domain.dependency as _d_dep
import providers.repository.dependencies as _p_dep


class AddDependencies:
    def __init__(self, repo: _p_dep.DependencyRepo = _p_dep.DependencyRepo()):
        self.repo = repo

    def __call__(
        self, project_id: str, dependencies: _t.List[_d_dep.Dependency]
    ) -> None:
        for dep_str in dependencies:
            if not "==" in dep_str:
                continue
            name, version = dep_str.split("==", 1)
            dependency = _d_dep.Dependency(
                project_id=project_id,
                name=name.strip(),
                version=version.strip(),
            )
            self.repo.add_dependency(dependency)
