from pydantic import BaseModel
from typing import Optional

class DeviceInfo(BaseModel):
    token: str
    username: Optional[str]

    class Config:
        orm_mode = True


class Configuration(BaseModel):
    modelUrl: str
    frequency: int
    federated: bool

    class Config:
        orm_mode = True