from datetime import datetime
from sqlalchemy import ForeignKey, String  # String 추가
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.model.base import Base

class Pds(Base):
    __tablename__ = 'pds'

    pno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(100), index=True)  # 길이 지정
    userid: Mapped[str] = mapped_column(ForeignKey('member.userid'), index=True)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    views: Mapped[int] = mapped_column(default=0)
    contents: Mapped[str] = mapped_column(String(500))  # 길이 지정
    # back_populates 양방향 관계 설정
    attachs = relationship('PdsAttach', back_populates='pds')  # 하나의 갤러리는 하나 이상의 첨부파일(attach)이 존재 가능 (1:n)


class PdsAttach(Base):
    __tablename__ = 'pdsattach'

    pano: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    pno: Mapped[int] = mapped_column(ForeignKey('pds.pno'), index=True)
    fname: Mapped[str] = mapped_column(String(100), nullable=False)  # 길이 지정
    fsize: Mapped[int] = mapped_column(default=0)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    pds: Mapped[Pds] = relationship('Pds', back_populates='attachs')  # 하나의 첨부파일(attach)는 하나의 갤러리에 속함 (1:1)
