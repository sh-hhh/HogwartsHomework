import requests


class BaseApi:
    _CORPID = "ww873e410f7ada69e6"
    _CORPSECRET = "b5z7hK2u3iYfv4mrDioOsTj9eArlaWuafzoi_WwDSy4"
    _BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/"

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        """
        获取token
        :return:
        """
        result = self.send_request("GET", f"gettoken?corpid={self._CORPID}&corpsecret={self._CORPSECRET}")
        return result.json().get("access_token")

    def send_request(self, method, url, **kwargs):
        """
        封装发送请求
        :param method: 请求方式
        :param url: 请求地址
        :param kwargs:
        :return:
        """
        url = self._BASE_URL + url
        return requests.request(method, url, **kwargs)
