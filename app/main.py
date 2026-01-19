from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.api.explain import router as explain_router


app = FastAPI(title="ExplainLikeDev")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()
    
@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(explain_router, prefix="/api")
