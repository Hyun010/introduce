from flask import Flask, render_template
from database import db, Student
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
db.init_app(app)


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

if __name__ == '__main__':
    app.run(debug=True)


with app.app_context():
    db.create_all()