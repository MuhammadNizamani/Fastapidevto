from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="FastAPI course", version="0.0.1",docs_url='/')


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/ping")
def health_check():
    """Health check."""

    return {"message": "Hello I am working!"}