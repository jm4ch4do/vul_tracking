from providers.repository.base import BaseInMemoryRepo
import application.dependencies as _a_dep
import domain.dependency as _d_dep
import typing as _t


class DependencyRepo(BaseInMemoryRepo[_d_dep.Dependency], _a_dep.DependencyRepository):

    name = "name"
    version = "version"

    def __init__(self) -> None:
        super().__init__()

    def _to_entity(self, raw: dict) -> _d_dep.Dependency:
        return _d_dep.Dependency(
            id=raw[self.id],
            name=raw[self.name],
            version=raw[self.version],
        )

    def _serialize(self, entity: _d_dep.Dependency) -> dict:
        return {
            self.id: entity.id,
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
