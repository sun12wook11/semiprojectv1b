from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from app.model.base import Base

class board(Base):
    __tablename__ = 'board'  # 이 클래스가 매핑될 데이터베이스 테이블의 이름을 지정합니다.

    bno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(index=True)
    userid: Mapped[str] = mapped_column(ForeignKey('member.userid'), index=True)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    views: Mapped[int] = mapped_column(default=0)
    content: Mapped[str]


# 테이블 매핑
# 식별 관계