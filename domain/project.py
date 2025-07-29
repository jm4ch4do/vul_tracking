import datetime as _dt

import pydantic as _p


class Project(_p.BaseModel):
    id: str
    name: str
    description: str
    created_at: _dt.date

    @property
    def elapsed_time(self) -> _dt.timedelta:
        """Returns the time elapsed since the project was created."""
        return _dt.date.today() - self.created_at
