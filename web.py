from flask import Flask, render_template, request
app = Flask(__name__)

# creates homepage
@app.route("/")
def index():
    return render_template('sample_page.html')

# Produces IP - runs web server
# 127.0.0.1 is the same as local host
# http://127.0.0.1:5000/ is localhost:5000/
# debug True allows you to change code w/out restarting server


@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)

# Git commands
# Untracked
# Tracked
# Staged 
# Committed

# {{ Will insert Python code into HTML}}
