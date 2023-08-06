from Job import Job
from JobProgress import JobProgress
from typing import Optional, Any
from pydantic import BaseModel, Field
class CurrentJob(BaseModel): 
  job: Job = Field()
  progress: JobProgress = Field()
  state: str = Field()
  error: Optional[str] = Field()
