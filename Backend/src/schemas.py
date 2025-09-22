from pydantic import BaseModel

class ResumeData(BaseModel):
    name: str
    email: str
    phone: str
    education: str
    experience: str
    skills: str