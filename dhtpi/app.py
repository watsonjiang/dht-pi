import asyncio
from .log import LOGGER

def app_main():
    """
    主循环, 读取设备, 并将数据写入数据库.
    :return:
    """
    loop = asyncio.get_event_loop()

    try:
        loop.run_forever()
    except:
        LOGGER.exception("unexpected exception.")