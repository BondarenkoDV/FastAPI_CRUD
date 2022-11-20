from datetime import datetime
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    rubrics: list[str]
    text: str
    created_date: datetime

    class Config:
        schema_extra = {
            "example": {
                "id": 1501,
                "rubrics": [
                    "Что-то первое, что-то второе, и так далее"
                ],
                "text": "Любая строка",
                "created_date": "2022-11-17T15:25:27.063Z"
            }
        }
        orm_mode = True
