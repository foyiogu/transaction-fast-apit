from enum import Enum
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Role(str, Enum):
    admin: "admin"
    user: "user"


class User(BaseModel):
    id: Optional[int] = None
    # created_at: datetime = timestamp.timestamp(.)
    # updated_at: datetime = datetime.now()
    debitAccountId: str
    category: str
    product_type: str
    ranking: int
    role: Role

