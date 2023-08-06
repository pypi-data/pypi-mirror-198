
from typing import Optional, Any
from pydantic import BaseModel, Field
class JobStatus(BaseModel): 
  status: Optional[JobStatus] = Field()
