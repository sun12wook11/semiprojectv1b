from datetime import datetime

import mapped
from sqlalchemy.orm import Mapped, mapped_column

from app.model.base import Base


class Member(Base):
    __tablename__ = 'member'

    mno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    userid: Mapped[str] = mapped_column(index=True)
    passwd: Mapped[str]
    name: Mapped[str]
    email: Mapped[str]
    regdate: Mapped[str] = mapped_column(default=datetime.now)