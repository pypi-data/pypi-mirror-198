
from typing import Optional, Any
from pydantic import BaseModel, Field
class GcodeFile(BaseModel): 
  name: Optional[str] = Field()
  display: Optional[str] = Field()
  path: Optional[str] = Field()
  origin: Optional[str] = Field()
