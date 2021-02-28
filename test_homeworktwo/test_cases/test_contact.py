import json

from test_homeworktwo.api.contacts import Contacts
import pytest


class TestContacts:
    def setup(self):
        self.contact = Contacts()

    @pytest.mark.parametrize("userid, mobile", [("lihuanying1", "13312312301"), ("lihuanying2", "13312312302"),
                                                ("lihuanying3", "13312312303"), ("lihuanying4", "13312312304")])
    def test_add_member(self, userid, mobile):
        name = "今天是星期六_27"
        department = [1, 4]
        self.contact.delete_member(userid)
        self.contact.add_member(userid, name, mobile, department)
        self.contact.update_member(userid, "李焕英", department, mobile)
        r = self.contact.get_member(userid)
        j = json.dumps(r, indent=4, ensure_ascii=False)
        print(j)
        assert r.get("name", "错误") == "李焕英"