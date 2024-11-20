from flask import Flask
import database
from controllers.discipline import discipline_bp
from controllers.course import course_bp
from controllers.teacher import teacher_bp

app = Flask(__name__)

# DB
database.init()

# Register
app.register_blueprint(discipline_bp)
app.register_blueprint(course_bp)
app.register_blueprint(teacher_bp)

if __name__ == '__main__':
    app.run(debug=True)