from app import app
from fetch_data_model import fetch_data_model
obj = fetch_data_model()


@app.route("/fetch")
def signup_controller():
    return obj.get_data()