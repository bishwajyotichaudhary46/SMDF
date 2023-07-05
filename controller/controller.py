from app import app

@app.route("/")
def fetch():
    return "fetching"