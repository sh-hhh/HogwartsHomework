import logging
from typing import List


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


def add_logger():
    logging.basicConfig(level=logging.INFO,
                        # 日志格式
                        # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        # 打印日志的时间
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        # 日志文件存放的目录（目录必须存在）及日志文件名
                        filename='./logs/report.log',
                        # 打开日志文件的方式
                        filemode='w'
                        )
    logger = logging.getLogger(__name__)
    return logger


logger = add_logger()
