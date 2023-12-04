from fastapi import APIRouter, UploadFile, status
from sqlalchemy.orm import Session
from typing import Union, Optional, List
from models import SessionLocal, Message , get_db
from pydantic import BaseModel, HttpUrl, validator

router = APIRouter

class message(BaseModel):
    id: int
    name: str
    email: str
    message: str

    class Config:
        orm_mode = True

    
db = SessionLocal()

@router.post('/new_message', response_model = )