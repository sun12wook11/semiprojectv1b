from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from app.model.base import Base

class Gallery(Base):
    __tablename__ = 'gallery'

    gno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(100), index=True)  # 제목의 최대 길이 지정
    userid: Mapped[str] = mapped_column(ForeignKey('member.userid'), index=True)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    views: Mapped[int] = mapped_column(default=0)
    contents: Mapped[str] = mapped_column(String(500))  # 내용의 최대 길이 지정
    # back_populates 양방향 관계 설정
    attachs = relationship('GalAttach', back_populates='gallery')  # 하나의 갤러리는 하나 이상의 첨부파일(attach)이 존재 가능 (1:n)


class GalAttach(Base):
    __tablename__ = 'galattach'

    gano: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    gno: Mapped[int] = mapped_column(ForeignKey('gallery.gno'), index=True)
    fname: Mapped[str] = mapped_column(String(255), nullable=False)  # 파일 이름의 최대 길이 지정
    fsize: Mapped[int] = mapped_column(default=0)
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)
    gallery: Mapped[Gallery] = relationship('Gallery', back_populates='attachs')  # 하나의 첨부파일(attach)는 하나의 갤러리에 속함 (1:1)
