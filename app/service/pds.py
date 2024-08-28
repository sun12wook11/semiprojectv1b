from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.model.pds import PdsAttach


class PdsService:
    @staticmethod
    def selectone_file(db, pno):
        try:
            find_pno = PdsAttach.pno == pno
            stmt = select(PdsAttach).where(find_pno)
            result = db.execute(stmt).scalars().first()

            return result

        except SQLAlchemyError as ex:
            print(f'▶▶▶ selectone_gallery에서 오류발생 : {str(ex)} ')

