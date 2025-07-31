import datetime as _dt
import typing as _t
import uuid as _uuid

import application.projects as _a_pro
import domain.project as _d_pro


class ProjectRepo(_a_pro.ProjectRepository):

    id = "id"
    name = "name"
    description = "description"
    created_at = "created_at"

    _storage: _t.List[_t.Dict[str, _t.Any]] = []

    def list_projects(self) -> _t.List[_d_pro.Project]:
        return [self._to_entity(raw) for raw in self._storage]

    def populate(self, projects: _t.List[_d_pro.Project]) -> None:
        self._storage = [self._serialize(proj) for proj in projects]

    def clear(self) -> None:
        self._storage.clear()

    def add_project(self, project: _d_pro.Project) -> None:
        if not project.id:
            project.id = str(_uuid.uuid4())
        self._storage.append(self._serialize(project))

    def get_project_by_id(self, project_id: str) -> _t.Optional[_d_pro.Project]:
        for raw in self._storage:
            if raw[self.id] == project_id:
                return self._to_entity(raw)
        return None

    def remove_project(self, project_id: str) -> bool:
        for i, raw in enumerate(self._storage):
            if raw[self.id] == project_id:
                del self._storage[i]
                return True
        return False

    @classmethod
    def _to_entity(cls, raw: _t.Dict[str, _t.Any]) -> _d_pro.Project:
        return _d_pro.Project(
            id=raw[cls.id],
            name=raw[cls.name],
            description=raw[cls.description],
            created_at=_dt.datetime.strptime(raw[cls.created_at], "%Y-%m-%d").date(),
        )

    @classmethod
    def _serialize(cls, entity: _d_pro.Project) -> _t.Dict[str, _t.Any]:
        return {
            cls.id: entity.id,
            cls.name: entity.name,
            cls.description: entity.description,
            cls.created_at: entity.created_at.isoformat(),
        }

    @classmethod
    def from_entity(cls, project: _d_pro.Project) -> "ProjectRepo":
        instance = cls()
        instance._storage = [cls._serialize(project)]
        return instance
