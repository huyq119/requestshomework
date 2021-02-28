import requests


class Base:

    def __init__(self):
        corpid = "wwe46394ef41c1fbe3"
        corpsecret = "9iECP3c-crX1YAw1Is-WrkN2D8tfVOsZTGBch0p_BJQ"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        self.s = requests.Session()
        r = self.send("get", url)
        self.s.params = {'access_token': r.get("access_token")}

    def send(self, *args, **kwargs):
        r = self.s.request(*args, **kwargs)
        return r.json()
