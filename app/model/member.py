from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from app.model.base import Base

class Member(Base):
    __tablename__ = 'member'

    mno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    userid: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)  # 식별관계
    passwd: Mapped[str] = mapped_column(String(128), nullable=False)  # 패스워드 길이 지정
    name: Mapped[str] = mapped_column(String(50), nullable=False)  # 이름 길이 지정
    email: Mapped[str] = mapped_column(String(100), nullable=False)  # 이메일 길이 지정
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)  # 등록 날짜











