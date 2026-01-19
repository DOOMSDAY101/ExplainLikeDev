from fastapi import APIRouter
from pydantic import BaseModel
from app.core.explainer import explain_code

router = APIRouter()


class ExplainRequest(BaseModel):
    code: str
    experience_level: str


class ExplainResponse(BaseModel):
    explanation: str
    improvements: str
    common_mistakes: str



@router.post("/explain", response_model=ExplainResponse)
def explain_endpoint(request: ExplainRequest):
    return explain_code(
        code=request.code,
        experience_level=request.experience_level
    )
   

