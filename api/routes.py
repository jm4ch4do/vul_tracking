import fastapi as _fa
import api.projects as _projects

router = _fa.APIRouter()

@router.get("/")
def root():
    return {"message": "Hello from root"}

router.include_router(_projects.router, prefix="/api")