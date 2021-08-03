from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/featured')
def featured():
    return render_template('featured.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

if __name__ == '__main__':
    app.run(debug=True)