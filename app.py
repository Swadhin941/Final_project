from flask import Flask, request, render_template
app= Flask(__name__)


# #configure db
# app.secret_key = 'your secret key'

# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'log'
# app.config['MYSQL_HOST'] = 'localhost'
# mysql=MySQL(app)


@app.route('/')
def home():
    return render_template('Home.html')



@app.route('/signup')
def signup():
    return render_template('SignUp.html')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/blog')
def blog():
    return render_template('Blog.html')

if __name__ == '__main__':
    app.run(debug=True)