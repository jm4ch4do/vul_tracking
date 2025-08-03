import typing as _t

import pydantic as _p


class DependencyOutputDTO(_p.BaseModel):
    id: str
    project_id: str
    name: str
    version: str
    is_vul: bool


class VulOutputDTO(_p.BaseModel):
    osv_id: str
    modified: str


class DependencyAndVulsOutputDTO(_p.BaseModel):
    id: str
    project_id: str
    name: str
    version: str
    is_vul: bool
    vuls: _t.List[VulOutputDTO] = []
