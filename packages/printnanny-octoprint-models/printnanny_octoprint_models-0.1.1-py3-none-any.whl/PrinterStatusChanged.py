from PrinterStatus import PrinterStatus
from typing import Optional, Any
from pydantic import BaseModel, Field
class PrinterStatusChanged(BaseModel): 
  status: PrinterStatus = Field()
