# from pydantic import BaseModel

from sqlalchemy import String, Boolean, Integer, Column, DateTime, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from .database import Base
from passlib.hash import bcrypt

class Message(Base):
    __tablename__='messages'
    id=Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    email=Column(String, unique=True)
    message = Column(String, nullable=False)

    def __repr__(self):
        return f"<Message name={self.name} email={self.email} text={self.message}>"

class User(Base):
    __tablename__='users'
    id=Column(Integer, primary_key=True)
    name=Column(String)
    password_hash = Column(String)
    summary=Column(String)
    profile_pic=Column(LargeBinary)
    profile_url=Column(String, nullable=True)

    def __repr__(self):
        return f"<User <name = {self.name} summary = {self.summary}>"


class Technology(Base):
    __tablename__='technologies'
    id=Column(Integer, primary_key=True)
    name=Column(String)
    icon = Column(LargeBinary)
    icon_url = Column(String, nullable=True)
    

    def __repr__(self):
        return f"<User <icon = {self.name} >"
    

class Service(Base):
    __tablename__='services'
    id=Column(Integer, primary_key=True)
    title=Column(String)
    icon = Column(LargeBinary)
    icon_url = Column(String, nullable=True)
    

    def __repr__(self):
        return f"<User <title = {self.title} >"
    

class Experience(Base):
    __tablename__='experiences'
    id=Column(Integer, primary_key=True)
    title=Column(String)
    company_name=Column(String)
    icon = Column(String)
    icon_url = Column(String, nullable=True)
    iconBg = Column(String)
    points= Column(String)
    date = Column(DateTime)
    

    def __repr__(self):
        return f"<EXperience title = {self.title}  company = {self.company_name} points = {self.points}>"

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(String)
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship("Project", back_populates="tags")

    def __repr__(self):
        return f"<Tag id={self.id} name={self.name} color={self.color}>"


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)
    image_url=Column(String, nullable=True)
    source_code_link = Column(String)
    tags = relationship("Tag", back_populates="project")

    def __repr__(self):
        return f"<Project id={self.id} name={self.name} description={self.description} image={self.image} source_code_link={self.source_code_link}>"



