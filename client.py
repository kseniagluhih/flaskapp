import os
from io import BytesIO
import base64
import requests

path = os.path.join('./static', 'image01.png')
with open(path, 'rb') as fh:
    img_data = fh.read()
    b64 = base64.b64encode(img_data)

jsondata = {'imagebin': b64.decode('utf-8')}
res = requests.post('http://localhost:5000/apinet', json=jsondata)
if res.ok:
     print(res.json())

# import requests
# r = requests.get("http://localhost:5000/")
# print(r.status_code)
# print(r.text)
# r = requests.get("http://localhost:5000/data_to")
# print(r.status_code)
# print(r.text)
