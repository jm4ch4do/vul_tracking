import fastapi as _fa

import api.projects as _api_projects
import api.dependencies as _api_dep

router = _fa.APIRouter()


@router.get("/")
def root():
    return {"message": "Api is Alive. Try /docs# for the swagger"}


router.include_router(_api_projects.router, tags=["Projects"])
router.include_router(_api_dep.router, tags=["Dependencies"])
