from typing import Literal
import json
from pydantic import BaseModel, Field,ValidationError
class StockFilter(BaseModel):
    # required: which screen
    module: Literal["stock", "alloy_inward"]
    # optional filters (default None)
    metal: Literal["Gold", "Silver", "Platinum"] | None = None
    purity: Literal[
    "24K", "23K", "22K", "20K", "18K", "14K", "9K",   # gold
    "999", "970", "925", "900", "835", "800",          # silver
    "950",                                             # platinum
    ] | None = None
    category: str| None = None   # Ring / Chain / Bangle / Necklace / Earring
    branch:str|None=None    # any text
    weight_min: float |None = Field(default=None, gt=0)   # number, must be > 0
    weight_max: float |None = Field(default = None,gt=0)
f1 = StockFilter(module="stock", metal="Gold", purity="22K", branch="Chennai")
def parse_ai_output(text):
    # 1. try: convert text to dict with json.loads
    try:
        input = json.loads(text)
    # 2.      create a StockFilter from the dict (use **data)
  
    # 3.      return the StockFilter
        return StockFilter(**input)
    # 4. except json.JSONDecodeError: print "Invalid JSON", return None
    except json.JSONDecodeError:
        print('invalid json')
        return
    except ValidationError as e:
        print (e)
        return