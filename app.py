from flask import Flask, render_template, Response
from streamer import Streamer

app = Flask(__name__)

def gen():
  streamer = Streamer('178.138.193.180', 13919)
  streamer.start()

  while True:
    if streamer.streaming:
      yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + streamer.get_jpeg() + b'\r\n\r\n')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/video_feed')
def video_feed():
  return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')