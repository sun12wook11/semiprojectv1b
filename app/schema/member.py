from pydantic import BaseModel
class NewMember(BaseModel):
    userid: str
    passwd: str
    name: str
    email: str

# 유효성 검사