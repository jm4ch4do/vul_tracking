import pydantic as _p


class DependencyCreateDTO(_p.BaseModel):
    name: str
    version: str


class DependencyOutputDTO(_p.BaseModel):
    id: str
    name: str
    version: str
