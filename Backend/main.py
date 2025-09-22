from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware




from src.routes.resume_build import router as resume_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume_router)