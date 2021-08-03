from flask import Flask,render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return redirect(url_for('index'))

@app.route('/featured')
def featured():
    return render_template('featured.html')

@app.route('/acheivements')
def achievements():
    return render_template('acheivements.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)