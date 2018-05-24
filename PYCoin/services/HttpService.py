import json
import requests # $ pip3 install requests

class Http:
    def get(self, url):
        if (url == ""):
            return None
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return json.loads(response.content.decode('utf-8'))
        except:
            raise Exception("Fail to Open URL: %s", url)
        return None
