import typing as _t

import fastapi as _fa

from application import dependencies as _a_dep
from application import projects as _a_pro
from domain import project as _d_pro

router = _fa.APIRouter()


@router.get("/projects", response_model=_t.List[_a_pro.ProjectOutputDTO])
def list_projects():
    projects = _a_pro.GetProjects()()
    return [
        _a_pro.ProjectOutputDTO(**project.dict(), since_days=project.elapsed_time)
        for project in projects
    ]


@router.post(
    "/projects",
    status_code=_fa.status.HTTP_201_CREATED,
    response_model=_a_pro.ProjectOutputDTO,
)
def create_project(project_dto: _a_pro.ProjectCreateDTO):

    project = _d_pro.Project(
        id=None,
        name=project_dto.name,
        description=project_dto.description,
        created_at=project_dto.created_at,
    )

    _a_pro.AddProject()(project, dependencies=project_dto.dependencies or [])
    return _a_pro.ProjectOutputDTO(**project.dict(), since_days=project.elapsed_time)


@router.get(
    "/projects/{project_id}/dependencies",
    response_model=_t.List[_a_dep.DependencyOutputDTO],
    summary="Get dependencies for a project",
)
def get_project_dependencies(project_id: str):
    dependencies = _a_dep.GetDependenciesByProjectId()(project_id)
    return [_a_dep.DependencyOutputDTO(**dep.dict()) for dep in dependencies]
