import datetime as _dt
import typing as _t

import application.projects as _a_pro
import domain.project as _d_pro
from providers.repository.base import BaseInMemoryRepo


class ProjectRepo(BaseInMemoryRepo[_d_pro.Project], _a_pro.ProjectRepository):

    name = "name"
    description = "description"
    created_at = "created_at"

    def __init__(self) -> None:
        super().__init__()

    def _to_entity(self, raw: dict) -> _d_pro.Project:
        return _d_pro.Project(
            id=raw[self.id],
            name=raw[self.name],
            description=raw[self.description],
            created_at=_dt.datetime.strptime(raw[self.created_at], "%Y-%m-%d").date(),
        )

    def _serialize(self, entity: _d_pro.Project) -> dict:
        return {
            self.id: entity.id,
            self.name: entity.name,
            self.description: entity.description,
            self.created_at: entity.created_at.isoformat(),
        }

    def list_projects(self) -> _t.List[_d_pro.Project]:
        return self.list_all()

    def add_project(self, project: _d_pro.Project) -> None:
        self.add(project)

    def get_project_by_id(self, project_id: str) -> _t.Optional[_d_pro.Project]:
        return self.get_by_id(project_id)

    def remove_project(self, project_id: str) -> bool:
        return self.remove(project_id)
