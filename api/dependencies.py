import typing as _t

import fastapi as _fa

from application import dependencies as _a_dep

router = _fa.APIRouter()


@router.get("/dependencies", response_model=_t.List[_a_dep.DependencyOutputDTO])
def list_dependencies():
    dependencies = _a_dep.GetDependencies()()
    return [_a_dep.DependencyOutputDTO(**dep.dict()) for dep in dependencies]


@router.get(
    "/update_vuls",
    summary="Triggers task update vulnerable dependencies and projects",
)
def scan_dependencies():
    vuls = _a_dep.UpdateVuls()()
    return "Task ran successfully"
