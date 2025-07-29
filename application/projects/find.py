import typing as _t

import domain.project as _d_pro
import providers.repository.projects as _p_projects


class GetProjects:
    def __init__(self):
        self.repo = _p_projects.ProjectRepo()

    def __call__(self) -> _t.List[_d_pro.Project]:
        return self.repo.list_projects()
