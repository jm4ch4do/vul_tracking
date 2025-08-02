import typing as _t

import application.dependencies as _a_dep
import domain.dependency as _d_dep
from providers.repository.base import BaseInMemoryRepo


class DependencyRepo(BaseInMemoryRepo[_d_dep.Dependency], _a_dep.DependencyRepository):

    project_id = "project_id"
    name = "name"
    version = "version"

    def __init__(self) -> None:
        super().__init__()

    def _to_entity(self, raw: dict) -> _d_dep.Dependency:
        return _d_dep.Dependency(
            id=raw[self.id],
            project_id=raw[self.project_id],
            name=raw[self.name],
            version=raw[self.version],
        )

    def _serialize(self, entity: _d_dep.Dependency) -> dict:
        return {
            self.id: entity.id,
            self.project_id: entity.project_id,
            self.name: entity.name,
            self.version: entity.version,
        }

    def list_dependencies(self) -> _t.List[_d_dep.Dependency]:
        return self.list_all()

    def add_dependency(self, dependency: _d_dep.Dependency) -> None:
        self.add(dependency)

    def get_dependency_by_id(
        self, dependency_id: str
    ) -> _t.Optional[_d_dep.Dependency]:
        return self.get_by_id(dependency_id)

    def remove_dependency(self, dependency_id: str) -> bool:
        return self.remove(dependency_id)

    def list_dependencies_by_project_id(
        self, project_id: str
    ) -> _t.List[_d_dep.Dependency]:
        return [dep for dep in self.list_all() if dep.project_id == project_id]
