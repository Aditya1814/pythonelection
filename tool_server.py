from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Election Tools", version="1.0.0")

class VoterCountResponse(BaseModel):
    constituency: str
    total_voters: int

@app.get("/voter_count", response_model=VoterCountResponse)
def voter_count():
    return {"constituency": "Hyderabad", "total_voters": 234567}
