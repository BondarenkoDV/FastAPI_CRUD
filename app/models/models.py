from sqlalchemy import Column, Integer, ARRAY, String, Text, Date
from .database import Base


class Item(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    rubrics = Column(ARRAY(Text()), index=True)
    text = Column(String, index=True)
    created_date = Column(Date, index=True)
