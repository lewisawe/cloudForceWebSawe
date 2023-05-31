from flask import Flask, render_template

app = Flask(__name__)
visitors = 0

@app.route('/')
def index():
    global visitors
    visitors += 1
    return render_template('index.html', visitor_count=visitors)

if __name__ == '__main__':
    app.run()
