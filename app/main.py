from fastapi import FastAPI
from app.api.explain import router as explain_router


app = FastAPI(title="ExplainLikeDev")

@app.get("/")
def health_check():
    return {"status": "ok"}

app.include_router(explain_router, prefix="/api")
