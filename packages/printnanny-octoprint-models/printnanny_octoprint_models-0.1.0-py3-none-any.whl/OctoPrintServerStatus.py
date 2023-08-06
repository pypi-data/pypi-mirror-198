
from typing import Optional, Any
from pydantic import BaseModel, Field
class OctoPrintServerStatus(BaseModel): 
  additionalProperties: Optional[Any] = Field()
  status: Optional[OctoPrintServerStatus] = Field()
