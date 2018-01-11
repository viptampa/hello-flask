from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "Hello World"

<<<<<<< HEAD
app.run()
=======
app.run()
>>>>>>> f88436ac9a23af448d8dc22038e5689dedb8398e
