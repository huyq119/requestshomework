from test_homeworktwo.api.base import Base


class Contacts(Base):

    def add_member(self, userid: str, name: str, mobile: str, department: list, *args):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
        }
        return self.send("post", url, json=body)

    def get_member(self, userid: str):
        userid = userid
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send("get", url)

    def update_member(self, userid: str, name: str, department: list, mobile: str, *args):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile,
        }
        return self.send("post", url, json=body)

    def delete_member(self, userid: str):
        userid = userid
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send("get", url)
