from flask import Flask, render_template
import random
app = Flask(__name__)
images = [
  "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26388-1381844103-11.gif",
  "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr03/15/10/anigif_enhanced-buzz-11980-1381846269-1.gif"
]
@app.route('/')
def index():
  url= random.choice(images)
  return render_template('index.html', url=url)

if __name__ == "__main__":
   app.run(host="0.0.0.0")
