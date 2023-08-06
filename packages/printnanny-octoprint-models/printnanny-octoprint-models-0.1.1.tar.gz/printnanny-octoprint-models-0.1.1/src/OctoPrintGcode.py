from GcodeEvent import GcodeEvent
from typing import Optional, Any
from pydantic import BaseModel, Field
class OctoPrintGcode(BaseModel): 
  gcode: GcodeEvent = Field()
