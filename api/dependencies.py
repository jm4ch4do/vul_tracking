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


@router.get(
    "/dependencies/{dependency_id}",
    response_model=_a_dep.DependencyAndVulsOutputDTO,
    summary="Get dependencies details and vulnerabilities",
)
def get_dependencies(dependency_id: str):
    dependency, vuls = _a_dep.GetDependencyById()(dependency_id)
    vuls_dto = [_a_dep.VulOutputDTO(**vul.dict()) for vul in vuls]
    return _a_dep.DependencyAndVulsOutputDTO(**dependency.dict(), vuls=vuls_dto)
