from flask import Flask
app = Flask(__name__)

@app.route('/')
def write_to_file():
    with open('/data/message.txt', 'w') as f:
        f.write("Hello from Order Service!")
    return "Data written to /data/message.txt"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

