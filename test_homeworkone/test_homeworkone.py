import json

import requests


class TestHomeworkOne():

    corpid = "wwe46394ef41c1fbe3"
    corpsecret = "9iECP3c-crX1YAw1Is-WrkN2D8tfVOsZTGBch0p_BJQ"

    def setup(self):

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}"
        r = requests.get(url)
        self.access_token = r.json()["access_token"]

    def test_demo_add(self):

        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.access_token}"
        body = {
            "userid": "liudehua",
            "name": "刘德华",
            "alias": "AndyLau",
            "mobile": "+86 13366136613",
            "department": [1, 3],
            "order": [3, 3],
            "position": "首席运营官",
            "gender": "1",
            "email": "andylau@gzdev.com",
        }
        r = requests.post(url, json=body)
        j = r.json()
        json_dicts = json.dumps(j, indent=4, ensure_ascii=False)
        print("\n")
        print(json_dicts)

    def test_demo_update(self):

        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.access_token}"
        body = {
            "userid": "liudehua",
            "name": "刘德华",
            "department": [1,4],
            "order": [1,1],
            "position": "CTO",
            "mobile": "13699765656",
            "gender": "1",
        }
        r = requests.post(url, json=body)
        j = r.json()
        json_dicts = json.dumps(j, indent=4, ensure_ascii=False)
        print("\n")
        print(json_dicts)

    def test_demo_get(self):

        userid = "liudehua"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.access_token}&userid={userid}"
        r = requests.get(url)
        j = r.json()
        json_dicts = json.dumps(j, indent=4, ensure_ascii=False)
        print("\n")
        print(json_dicts)

    def test_demo_delete(self):

        userid = "liudehua"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.access_token}&userid={userid}"
        r = requests.get(url)
        j = r.json()
        json_dicts = json.dumps(j, indent=4, ensure_ascii=False)
        print("\n")
        print(json_dicts)