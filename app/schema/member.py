from pydantic import BaseModel


class NewMember(BaseModel):
    userid: str
    passwd: str
    passwdre: str
    name: str
    email: str


# 라우터에서 폼으로 만들어서 받을꺼냐
# 이렇게 스키마 맴버 클래스짜고 맴버 라우터 post json으로 받을꺼냐
