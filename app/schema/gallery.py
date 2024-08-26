from pydantic import BaseModel

class NewGallery(BaseModel):
    userid: str
    title: str
    contents: str
    # captcha: str

# 유효성 검사