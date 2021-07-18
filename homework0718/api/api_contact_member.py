from homework0718.api.base_api import BaseApi


class ApiContactMember(BaseApi):

    def add_member(self, userid, name, mobile, department, **kwargs):
        """
        添加成员
        :return:
        """
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        data.update(kwargs)
        result = self.send_request("POST", f"user/create?access_token={self.token}", json=data)
        return result

    def get_member(self, userid):
        """
        获取成员
        :return:
        """
        result = self.send_request("GET", f"user/get?access_token={self.token}&userid={userid}")
        return result

    def update_member(self, userid, **kwargs):
        """
        更新成员
        :return:
        """
        data = {
            "userid": userid
        }
        data.update(kwargs)
        result = self.send_request("POST", f"user/update?access_token={self.token}", json=data)
        return result

    def delete_member(self, userid):
        """
        删除成员
        :return:
        """
        result = self.send_request("GET", f"user/delete?access_token={self.token}&userid={userid}")
        return result