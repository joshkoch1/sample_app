from flask import Flask, render_template
app = Flask(__name__)

# creates homepage
@app.route("/")
def index():
    return render_template('index.html')

# Produces IP - runs web server
# 127.0.0.1 is the same as local host
# http://127.0.0.1:5000/ is localhost:5000/
# debug True allows you to change code w/out restarting server
app.run(debug=True)

# Git commands
# Untracked
# Tracked
# Staged 
# Committed


