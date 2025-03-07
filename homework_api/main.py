from flask import Flask
from src import resume_manipulator

resume_manipulator.generate_resume()

app = Flask(__name__, static_url_path="", static_folder="public")

@app.route("/resume/generate", methods = ["POST"])
def generate_resume(): 
    return resume_manipulator.generate_resume()

@app.route("/")
def get_resume(): 
    return resume_manipulator.get_resume()

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)
