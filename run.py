from flask import Flask
from flask import request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1> <title>Not Found 404</title> Not Found 404</h1>  <img src=\"https://c.tenor.com/1FoUREMXTMIAAAAC/azzouz-madaniya.gif\" alt=\"this slowpoke moves\"  />"


def IP():
    ip = request.environ.get('HTTP_X_REAL_IP')
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return ip


@app.route('/getsurveys')
def user():
    if 'ip' in request.args:
        ip_adr = request.args.get('ip')
        url = "https://wss.pollfish.com/v2/device/register/true?json={\"ip\": \"" \
              + ip_adr + "\",\"api_key\": " \
                         "\"ba6104f8-0d4f-4017-8d0b-aa6f73a7887f\",\"debug\": \"true\",\"device_id\": \"bfb3de2cc3f82505\"," \
                         "\"timestamp\": 1645448842,\"encryption\": \"NONE\",\"version\": 7,\"os\": 0,\"content_type\": \"json\"," \
                         "\"offerwall\": \"true\",\"device_descr\": \"android.os.Build.MODEL\"}&dontencrypt=true&debug=true"
        data = requests.request("GET", url)
        return {"code": data.status_code, 'ip': ip_adr, "responses": data.text}
    else:
        return {"code": 500, 'ip': get_client_ip(), "responses": 'IP parameter not present'}


@app.route('/get_client_ip')
def get_client_ip():
    ip = request.environ.get('HTTP_X_REAL_IP')
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return {'ip': ip}
