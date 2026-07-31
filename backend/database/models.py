from typing import List, Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import func, Text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__ = "Todo"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    # below is an optional or allowed a null value
    description: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(insert_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"Todo(id={self.id!r}, name={self.name!r})"
