from flask import Flask

from app.db.base import create_db
from app.routes import pizza_route
from app.data.password import ADMIN_PASS


app = Flask(__name__)
app.secret_key = ADMIN_PASS
app.register_blueprint(pizza_route)

def main():
    create_db()
    app.run(debug=True,port=2334)