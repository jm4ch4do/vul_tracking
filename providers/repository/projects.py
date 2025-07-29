import datetime as _dt
import typing as _t

import application.projects as _a_pro
import domain.project as _d_pro

_raw_projects = [
    {
        "id": "1",
        "name": "Apollo",
        "description": "Moon mission",
        "created_at": "2024-01-10",
    },
    {
        "id": "2",
        "name": "Mars Rover",
        "description": "Exploring Mars",
        "created_at": "2024-06-01",
    },
]


def to_entity(raw: _t.Dict[str, _t.Any]) -> _d_pro.Project:
    return _d_pro.Project(
        id=raw["id"],
        name=raw["name"],
        description=raw["description"],
        created_at=_dt.datetime.strptime(raw["created_at"], "%Y-%m-%d").date(),
    )


def from_entity(entity: _d_pro.Project) -> _t.Dict[str, _t.Any]:
    return {
        "id": entity.id,
        "name": entity.name,
        "description": entity.description,
        "created_at": entity.created_at.isoformat(),
    }


def list_raw_projects() -> _t.List[_t.Dict[str, _t.Any]]:
    return _raw_projects


class ProjectRepo(_a_pro.ProjectRepository):
    def list_projects(self) -> _t.List[_d_pro.Project]:
        raw_projects = list_raw_projects()
        return [to_entity(raw) for raw in raw_projects]
