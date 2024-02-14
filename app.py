from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/박성현/')
def myPage():
    # name 을 통한 데이터 조회
    context = {

    }
    return render_template('myPage.html', data=context)

@app.route('/<name>/')
def profile(name):
    # name 을 통한 데이터 조회
    context = {

    }
    return render_template('profile.html', data=context)


if __name__ == '__main__':
    app.run(debug=True)