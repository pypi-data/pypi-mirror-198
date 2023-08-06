
from typing import Optional, Any
from pydantic import BaseModel, Field
class JobProgress(BaseModel): 
  completion: Optional[float] = Field()
  filepos: Optional[int] = Field()
  printTime: Optional[int] = Field()
  printTimeLeft: Optional[int] = Field()
  printTimeLeftOrigin: Optional[str] = Field()
