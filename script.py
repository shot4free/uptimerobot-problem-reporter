
import http.client
import json
import ast
from gtts import gTTS
import subprocess

language = 'pl'

def pp_json(json_string):
#    print(json.dumps(json.loads(json_string), sort_keys=False, indent=4))
    return

conn = http.client.HTTPSConnection("api.uptimerobot.com")

payload = "api_key=YOUR_API_KEY_HERE&format=json&logs=0&statuses=9"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}

conn.request("POST", "/v2/getMonitors", payload, headers)

res = conn.getresponse()
data = res.read()

js = json.loads(data)

for key, value in js.items():
    if key == "monitors":
        if len(value) > 0:
            for x in range(len(value)):
                st = str(value[x])
                print(st)

                dct = ast.literal_eval(st)
                alarm = "UWAGA, devopsi! Rozjebał śię serwer"+ (dct['friendly_name'])
                myobj = gTTS(text=alarm, lang=language, slow=False)
                myobj.save("message.mp3")
                audio_file = "message.mp3"
                return_code = subprocess.call(["afplay", audio_file])

