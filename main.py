import fastapi as _fa

import api.routes as _routes

app = _fa.FastAPI()

app.include_router(_routes.router)
