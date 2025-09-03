from bottle import Bottle, run, template

app = Bottle()

@app.route('/')
def index():
    return template('<b>Welcome to the simple forum!</b>')

if __name__ == "__main__":
    run(app, host='localhost', port=8080)
