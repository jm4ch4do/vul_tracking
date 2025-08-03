import pydantic as _p


class DependencyOutputDTO(_p.BaseModel):
    id: str
    project_id: str
    name: str
    version: str
    is_vul: bool
