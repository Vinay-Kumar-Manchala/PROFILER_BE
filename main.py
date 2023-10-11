"""
This is the main script where Fast API application is initialized and routes are registered.
"""
import gc
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from scripts.constants import app_configuration

gc.collect()

tags_meta = [{"name": "Profiler", "description": "Services related to Profiler"}]
app = FastAPI(
    title="Profiler",
    version="v1.0",
    description="Profiler",
    openapi_tags=tags_meta
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[app_configuration.ALLOW_ORIGINS],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=["*"],
)


@app.get("/heart_beat")
def beats():
    return {"status": 200, "message": "My heart is beating.... adhola.."}