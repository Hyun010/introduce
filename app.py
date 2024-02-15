from flask import Flask, render_template, request, jsonify
from database import db, Student, Bookmark
import os, requests

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
db.init_app(app)

def check_six(st):
    words = {"ㅗ":"h", "ㄷ":"e", "ㅣ":"l", "ㅐ":"o", "디":"el"}
    code = ""
    for s in st:
        if s in words:
            code += words[s]
        else:
            code += s
    if code.lower() == "hello":
        return True
    return False

@app.route('/')
def home():
    s = Student.query.all()
    context = {
        "stus" : s
    }
    return render_template('index.html', data=context)

@app.route('/<name>/')
def profile(name):
    # name 을 통한 데이터 조회
    s1 = Student.query.filter_by(name=name).first()
    context = {
        "stu" : s1
    }
    return render_template('profile.html', data=context)

@app.route('/bookmark/', methods=['GET', 'POST', 'DELETE'])
def book():
    if request.method == "POST":
        data = request.json
        site_name, site_url, writer, managecode = data['site_name'], data['site_url'], data['writer'], data['managecode']
        print(managecode)
        if check_six(managecode):
            try:
                status = requests.get(site_url).status_code 
            except:
                return jsonify({'message': '사이트 요청이 불가한 URL 입니다. URL을 검토해주세요.'}), 500
            if status != 404:
                b = Bookmark(site_name=site_name, site_url=site_url, writer=writer)
                db.session.add(b)
                db.session.commit()
                return "", 200
            else:
                return jsonify({'message': '사이트 요청이 불가한 URL 입니다. URL을 검토해주세요.'}), 500
        else:
            return jsonify({'message': '관리자 생성코드 오류입니다.'}), 500
        
    elif request.method == "DELETE":
        data = request.json.get('value')
        if check_six(data[1]):
            b = Bookmark.query.filter_by(id=data[0]).first()
            db.session.delete(b)
            db.session.commit()
            return "", 200
        else:
            return jsonify({'message': '관리자 생성코드 오류입니다.'}), 500
        
    b = Bookmark.query.order_by(Bookmark.hits.desc()).all()
    context = {
        "books" : b    
    }
    return render_template('bookmark.html', data=context)

@app.route('/add_hits/', methods=["POST"])
def add_hits():
    data = request.json.get('value')
    b = Bookmark.query.filter_by(site_name=data[0], writer=data[1]).first()
    b.hits += 1
    db.session.add(b)
    db.session.commit()
    return "", 204



if __name__ == '__main__':
    app.run(debug=True)


with app.app_context():
    db.create_all()