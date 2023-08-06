from OctoPrintServerStatus import OctoPrintServerStatus
from typing import Optional, Any
from pydantic import BaseModel, Field
class OctoPrintServerStatusChanged(BaseModel): 
  status: OctoPrintServerStatus = Field()
