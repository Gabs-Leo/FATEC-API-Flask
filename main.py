from flask import Flask
import database
from controllers.discipline import discipline_bp

app = Flask(__name__)

# DB
database.init()

# Register
app.register_blueprint(discipline_bp)

if __name__ == '__main__':
    app.run(debug=True)