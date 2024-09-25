from datetime import datetime
from sqlalchemy import ForeignKey, String  # String 추가
from sqlalchemy.orm import Mapped, mapped_column
from app.model.base import Base

class Member(Base):
    __tablename__ = 'member'

    mno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    userid: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)  # 식별관계
    passwd: Mapped[str] = mapped_column(String(100))  # 비밀번호 길이 지정
    name: Mapped[str] = mapped_column(String(50))  # 이름 길이 지정
    email: Mapped[str] = mapped_column(String(100))  # 이메일 길이 지정
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)











