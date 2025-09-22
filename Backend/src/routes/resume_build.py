from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse
from pydantic import BaseModel
from src.services.resume_build import resume_service
import os
from src.schemas import ResumeData



router = APIRouter(prefix="/api/resume_build", tags=["Resume Build"])

@router.post("/generate_resume")
def generate_resume(data: ResumeData):
    try:
        pdf_path = resume_service.create_resume(data.dict())
        return FileResponse(
            pdf_path,
            media_type="application/pdf",
            filename="resume.pdf"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))