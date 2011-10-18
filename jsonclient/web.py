import os
import simplejson
import requests
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    jsonString = requests.get(os.environ.get("JSON_SERVICE_URL", "http://localhost:9000"))
    widgets = simplejson.loads(jsonString.content)
    htmlResponse = "<html><body>"
    for widget in widgets:
        htmlResponse += "Widget " + str(widget['id']) + " = " + widget['name'] + "</br>"
    htmlResponse += "</body></html>"
    return htmlResponse

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
