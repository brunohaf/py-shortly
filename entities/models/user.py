from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Optional
from sqlalchemy.sql import func
from pydantic import Field, BaseModel

from config.database import Base

# TO-DO: Add is_active column
class User(Base):
    
    __tablename__ = "Users"

    id: int = Column(Integer, primary_key=True)
    username: str = Column(default=None, nullable=False)
    hashed_password: str = Column(default=None, nullable=False)
    # is_active: bool = Column(default=True)
    created_at: Optional[datetime] = Column(
        default=None, server_default= func.now())
    updated_at: Optional[datetime] = Column(
        default=None, onupdate=func.now())
    
    urls = relationship("Url", back_populates='owner')

    def onupdate(self):
        self.updated_at = func.now()

class UserRequest(BaseModel):
    id: Optional[int] = Field(default=None)
    username: str = Field(default=None, nullable=False)
    password: str = Field(default=None, nullable=False)

    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "password"
            }
        }

# CREATE TABLE Users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(255) NOT NULL,
#     hashed_password VARCHAR(255) NOT NULL,
#     is_active BOOLEAN DEFAULT True,
#     created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#     updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
# )