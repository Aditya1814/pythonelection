from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

app = FastAPI(title="Election Tools", version="1.0.0")


# ✅ Response model
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


# ✅ FULL OpenAPI Override (Forces 3.0.3)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    schema = get_openapi(
        title="Election Tools",
        version="1.0.0",
        routes=app.routes,
    )

    # ✅ Force version manually
    schema["openapi"] = "3.0.3"

    # ✅ Add servers (Agent Builder expects this)
    schema["servers"] = [
        {"url": "https://pythonelection-1.onrender.com"}
    ]

    app.openapi_schema = schema
    return schema


app.openapi = custom_openapi
