import typing as _t

import fastapi as _fa

from application import projects as _a_pro

router = _fa.APIRouter()


@router.get("/projects", response_model=_t.List[_a_pro.ProjectOutputDTO])
def list_projects():
    projects = _a_pro.GetProjects()()
    return [
        _a_pro.ProjectOutputDTO(**project.dict(), since_days=project.elapsed_time)
        for project in projects
    ]
