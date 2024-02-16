import asyncio

from .dht11 import read_device
from .log import LOGGER, init_logging
from .db import db_init, append_dht_hist


async def _app_init():
    """
    初始化.
    :return:
    """
    init_logging()
    # 初始化数据库
    await db_init()


async def _main_loop():
    """
    主循环, 读取设备, 并将数据写入数据库.
    :return:
    """
    while True:
        try:
            # 读取设备
            humidity, temp = await read_device()
            # 写入数据库
            await append_dht_hist(humidity, temp)
            LOGGER.info(f"append_dht_hist: humidity={humidity}, temperature={temp}")
        except:
            LOGGER.exception("unexpected exception.")
        await asyncio.sleep(10)


async def app_main():
    """
    主入口
    :return:
    """
    try:
        await _app_init()
        await _main_loop()
    except:
        LOGGER.exception("unexpected exception.")
