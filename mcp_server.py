from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

app = FastAPI(title="Election Tools", version="1.0.0")


class VoterCountResponse(BaseModel):
    constituency: str
    total_voters: int


@app.get(
    "/voter_count",
    response_model=VoterCountResponse,
    operation_id="voter_count_tool"
)
def voter_count():
    return {"constituency": "Hyderabad", "total_voters": 234567}


# ✅ Custom OpenAPI for Agent Builder
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    schema = get_openapi(
        title="Election Tools",
        version="1.0.0",
        routes=app.routes,
    )

    # ✅ Force OpenAPI 3.0.3
    schema["openapi"] = "3.0.3"

    # ✅ Dynamic server URL (no hardcoding)
    schema["servers"] = [{"url": "/"}]

    app.openapi_schema = schema
    return schema


app.openapi = custom_openapi
