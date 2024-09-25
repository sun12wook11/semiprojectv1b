from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.model.base import Base

class Board(Base):
    __tablename__ = 'board'

    bno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(100), index=True)  # 제목의 최대 길이 지정
    userid: Mapped[str] = mapped_column(ForeignKey('member.userid'), index=True)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    views: Mapped[int] = mapped_column(default=0)
    contents: Mapped[str] = mapped_column(String(1000))  # 내용의 최대 길이 지정












