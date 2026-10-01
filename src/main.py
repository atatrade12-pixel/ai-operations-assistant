from fastapi import FastAPI

app = FastAPI(
    title="AI Operations Assistant",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "name": "AI Operations Assistant",
        "status": "ok",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }