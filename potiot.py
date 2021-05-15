import requests
import json


url = 'https://w0zawosezd.execute-api.eu-west-2.amazonaws.com/prod/uploadUrl'

def potiot_upload(deviceID, privateKey, fileType, filePath):
    param = {'deviceId': deviceID,
             'privateKey': privateKey,
             'fileType': fileType}
    
    res = requests.post(url, data = param) # POST to get upload URL
    #print(res.text) # print the response text

    if res.status_code == 200:
        res_json = json.loads(res.text)
        upload_url = res_json["url"]
        #print(upload_url) # print the temporary upload url
        result = requests.put(upload_url, data=open(filePath, 'rb'))
        #print(result)
        return result.status_code
    else:
        return res.status_code
