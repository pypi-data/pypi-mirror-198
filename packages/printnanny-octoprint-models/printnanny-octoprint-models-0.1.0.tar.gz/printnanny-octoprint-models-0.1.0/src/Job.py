from GcodeFile import GcodeFile
from typing import Optional, Any
from pydantic import BaseModel, Field
class Job(BaseModel): 
  file: Optional[GcodeFile] = Field()
  estimatedPrintTime: Optional[str] = Field()
  lastPrintTime: Optional[str] = Field()
  filamentLength: Optional[str] = Field()
  filamentVolume: Optional[str] = Field()
