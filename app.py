from flask import Flask
from users import users_bp
from courses import courses_bp

app = Flask(__name__)
app.register_blueprint(users_bp)
app.register_blueprint(courses_bp)

if __name__ == '__main__':
    app.run(debug=True)
