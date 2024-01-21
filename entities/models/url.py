from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Optional
from sqlalchemy.sql import func
from pydantic import BaseModel, Field

from config.database import Base


class Url(Base):
    __tablename__ = "Urls"

    id = Column(String, primary_key=True)
    original_url = Column(String, unique=True, index=True)
    created_at: Optional[datetime] = Column(
        default=None, server_default= func.now())
    last_accessed_at: Optional[datetime] = Column(
        default=None, onupdate=func.now())
    owner_id = Column(Integer, ForeignKey("Users.id"))

    owner = relationship("User", back_populates="urls")

    def onupdate(self):
        self.last_accessed_at = func.now()
    
class UrlRequest(BaseModel):
    user_id: int = Field(default=None, nullable=False)
    url: str = Field(default=None, nullable=False)


    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "1",
                "url": "https://www.google.com"
            }
        }

# CREATE TABLE Urls (
#     id VARCHAR(255) PRIMARY KEY,
#     original_url VARCHAR(255) NOT NULL,
#     owner_id int NOT NULL,
#     created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#     last_accessed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (owner_id) REFERENCES Users(id)        
# )