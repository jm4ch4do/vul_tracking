import datetime as _dt
import typing as _t

import pydantic as _p


class ProjectCreateDTO(_p.BaseModel):
    name: str
    description: str
    created_at: _t.Optional[_dt.date] = _p.Field(default_factory=_dt.date.today)
    dependencies: _t.List[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "My Test Project",
                "description": "A sample project for testing dependencies",
                "created_at": "2025-08-02",
                "dependencies": ["django==2.2.10", "requests==2.18.4", "pytest==7.4.0"],
            }
        }


class ProjectOutputDTO(_p.BaseModel):
    id: str
    name: str
    description: str
    created_at: _dt.date
    since_days: _dt.timedelta

    @_p.field_serializer("since_days", return_type=int)
    def serialize_since(self, td: _dt.timedelta, _info):
        return td.days
