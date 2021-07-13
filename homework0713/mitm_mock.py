import json

import mitmproxy
from mitmproxy import http


class MapLocalM:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url \
                and "x=" in flow.request.pretty_url:
            with open("quote.json", encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(
                    200,
                    f.read()
                )


class Rewrite:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url \
                and "x=" in flow.request.pretty_url:
            data = json.loads(flow.response.text)
            percent_list = [0, -0.1, 0.1]
            n = 0
            # 取前3只股票
            for item in data['data']['items'][:3]:
                item['quote']['percent'] = percent_list[n]
                n += 1
            flow.response.text = json.dumps(data)


addons = [
    MapLocalM(),
    Rewrite()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    mitmdump(['-p', '8080', '-s', __file__])
