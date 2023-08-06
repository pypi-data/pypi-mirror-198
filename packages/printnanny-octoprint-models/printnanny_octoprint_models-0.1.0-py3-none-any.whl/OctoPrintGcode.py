from GcodeEvent import GcodeEvent
from typing import Optional, Any
from pydantic import BaseModel, Field
class OctoPrintGcode(BaseModel): 
  gcode: Optional[GcodeEvent] = Field()
