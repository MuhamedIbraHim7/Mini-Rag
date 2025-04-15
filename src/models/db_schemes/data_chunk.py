from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId


class DataChunk(BaseModel):
    _id: Optional[ObjectId]
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId
    
    
    @validator('chunk_id')
    def validate_chunk_id(cls, value):
        if not value.isalnum():
            raise ValueError('chunk_id must be alphanumeric')
        return value

    class Config:
        arbitrary_types_allowed = True