import fastapi as _fa

router = _fa.APIRouter()

@router.get("/projects")
def list_projects():
    return [{"name": "Project A"}, {"name": "Project B"}]