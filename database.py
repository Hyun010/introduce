from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sex = db.Column(db.String)
    mbti = db.Column(db.String)
    life = db.Column(db.String)
    intro = db.Column(db.String)
    style = db.Column(db.String)
    prom = db.Column(db.String)
    loca = db.Column(db.String, nullable=False)
    blog = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    hob = db.Column(db.String)
    image = db.Column(db.String)
    role = db.Column(db.String)
    keyword = db.Column(db.String)

    def __repr__(self):
        return  f"{self.age} 세 {self.loca} 거주중인 {self.name} 님"

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String, nullable=False)
    site_url = db.Column(db.String, nullable=False)
    hits = db.Column(db.Integer, default=0)
    writer = db.Column(db.String, nullable=False, default="Unknown")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f"{self.writer} 가 작성한 {self.site_name}"
    


#     이름(name) : 정윤기
# 성별(sex) : 남
# MBTI(mbti) : INTJ
# 좌우명(life) : 잘먹고 잘살자
# 자기소개(intro) : 다른 사람과 비교 하지 않고 모르는 것은 배우며 내것으로 만드는 사람
# 협업스타일(style) : 함께 만들어 가며 배운다는 생각으로 서로 도와가며 한다.
# 개발자포부(prom) : 늦은 나이에 시작 했지만 남들보다 더열심히 노력 하여 개발 산업에 보탬이 될 수 있는 사람이 되겠습니다.
# 블로그 주소(blog) : https://blog.naver.com/jygmyjesus
# 사는지역(loca) : 충북 진천
# 나이(age) : 35(만33)
# 취미(hob) : 게임, 독서
# 역할(role) : 팀원
# 장점(키워드)(keyword) : 긍정적 사고방식


s1 = Student(name="정윤기", sex="남", mbti="INTJ", life="""잘먹고 잘살자""", intro="""다른 사람과 비교 하지 않고 모르는 것은 배우며 내것으로 만드는 사람""", 
                style="""소함께 만들어 가며 배운다는 생각으로 서로 도와가며 한다.""", prom="""늦은 나이에 시작 했지만 남들보다 더열심히 노력 하여 개발 산업에 보탬이 될 수 있는 사람이 되겠습니다.""",
                blog="https://blog.naver.com/jygmyjesus", loca="충북", hob="게임, 독서",
                            age=35, image="six_sense_jyg.png", role="팀원", keyword="긍정적 사고방식")
# 이름(name), 성별(sex), MBTI(mbti), 좌우명(life), 자기소개(intro), 협업스타일(style), 
# 개발자포부(prom), 블로그 주소(blog),사는지역(loca),나이(age),취미(hob),이미지(image),역할(role),장점(키워드)(keyword)