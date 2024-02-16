# 数据库模型
import functools

from .log import LOGGER

from sqlalchemy import Column, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.sqltypes import DateTime, FLOAT, Integer, String, DECIMAL

STOCK_DB = 'sqlite+aiosqlite:///stock_pi.sqlite3'

Base = declarative_base()


class DhtHist(Base):
    ''' 温湿度信息
    '''
    __tablename__ = 't_humidity_temp_hist'

    id = Column(Integer, primary_key=True)
    humidity = Column(DECIMAL)
    temperature = Column(DECIMAL)
    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, server_default=func.now(), server_onupdate=func.now())


_db_engine = None


async def db_init(db_url=None):
    # an Engine, which the Session will use for connection
    # resources
    global _db_engine
    _db_engine = create_async_engine(db_url if db_url else STOCK_DB)
    await _create_all_tables(_db_engine)


async def _create_all_tables(db_engine):
    """建表
    """
    async with db_engine.begin() as conn:
        # await conn.run_async(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def _with_session(c):
    async_session = sessionmaker(_db_engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as sess:
        return await c(sess)


async def _append_dht_hist(sess, humidity, temp):
    async with sess.begin():
        hist = DhtHist(humidity=humidity, temperature=temp)
        sess.add(hist)


async def append_dht_hist(humidity, temp):
    await _with_session(functools.partial(_append_dht_hist, humidity=humidity, temp=temp))
