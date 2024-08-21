from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError

from app.model.member import Member

class MemberService:
    @staticmethod
    def insert_member(db, member):
        try:
            # 정상적 실행 구간
            stmt = insert(Member).values(
                userid=member.userid, passwd=member.passwd,
                name=member.name, email=member.email)
            result = db.execute(stmt)
            db.flush()
            db.commit()
            return result

        except SQLAlchemyError as ex:
            # 오류발생 시 실행 구간
            print(f'▶▶▶ insert_member 오류발생: {str(ex)}')
            db.rollback()


# memberCRUD - 인서트 구현