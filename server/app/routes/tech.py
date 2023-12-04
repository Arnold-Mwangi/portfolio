from fastapi import APIRouter, UploadFile, status, Depends, HTTPException, File
from pydantic import BaseModel, HttpUrl, validator
from typing import Union, Optional, List
from sqlalchemy.orm import Session
from models import Technology, get_db, SessionLocal

import os

router = APIRouter()

class TechView(BaseModel):
    id: int
    name: str
    icon: str
    icon_url: str

    class Config:
        orm_mode = True

class TechCreate(BaseModel):
    name: str
    icon: UploadFile = File(None)
    icon_url: Optional[HttpUrl] = None 

    @validator('icon', pre=True, always=True)
    def at_least_one_field(cls, v, values):
        if v is None and values.get('icon_url') is None:
            raise ValueError("At least one of 'icon' or 'icon_url' must be provided")
        return v
    
    class Config:
        orm_mode = True

def save_icon(technology: TechCreate):
    if technology.icon:
        folder_path = "technology_icons"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, technology.icon.filename)
        with open(file_path, 'wb') as f:
            f.write(technology.icon.file.read())
        return file_path
    elif technology.icon_url:
        # You may want to add logic here to download the image from the URL if needed
        return technology.icon_url
    else:
        return None

class TechUpdate(BaseModel):
    id: Optional[int]
    name: Optional[str]
    icon: Union[UploadFile, HttpUrl, None] = None
    icon_url: Union[HttpUrl, None ] = None

    class Config:
        orm_mode = True

db = SessionLocal()

@router.post('/new_technology', response_model=TechCreate, status_code=status.HTTP_201_CREATED)
async def add_technology(
    technology: TechCreate,
    db: Session = Depends(get_db),
    file: UploadFile = File(...),  # Use the dependency for file uploads
):
    try:
        icon_path = save_icon(file)
        new_technology = Technology(
            name=technology.name,
            icon_url=icon_path
        )
        db.add(new_technology)
        db.commit()
        db.refresh(new_technology)
        return new_technology
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.put('/edit/technology/{tech_id}')
async def update_technology(tech_id: int):
    pass

@router.delete('delete/technology/{tech_id}')
async def delete_technology(tech_id:int):
    pass


@router.get('/technologies', response_model=List[TechView], status_code=200)
async def get_all_technologies():
    technologies = db.query(Technology).all()

    return technologies
