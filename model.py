from sqlalchemy import Column,Integer,String,Text,ForeignKey,DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
import enum


# define the status of ticket
class StatusEnum(str,enum.Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

# define PriorityEnum
class PriorityEnum(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    created_by = Column(Integer,ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)


class Issue(Base):
    __tablename__ = "issues"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    status = Column(Enum(StatusEnum), default=StatusEnum.OPEN)
    priority = Column(Enum(PriorityEnum))
    project_id = Column(Integer,ForeignKey("project_id"))
    assigned_by = Column(Integer, ForeignKey("users_id"))
    created_by = Column(DateTime, default=datetime.utcnow)


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    issue_id = Column(Integer,ForeignKey("issues_id"))
    user_id = Column(Integer, ForeignKey("users_id"))
    message = Column(Text)
    created_by = Column(DateTime, default=datetime.utcnow)