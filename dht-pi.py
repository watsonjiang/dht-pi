#!/usr/bin/env python
# 启动一个后台精灵进程,
# 根据配置拉起stock-pi各个模块.

import argparse
import asyncio
import sys

from setproctitle import setproctitle

sys.path.append('')
from dhtpi.daemon import Daemon

PID_FILE = 'dht-pi.pid'

class DhtPiDaemon(Daemon):

    def run(self):
        setproctitle("dht-pi")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.run(app_main())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', help='start|stop|restart', choices=['start', 'stop', 'restart'])
    args = parser.parse_args()
    if args.cmd == 'start':
        DhtPiDaemon(PID_FILE).start()
    elif args.cmd == 'stop':
        DhtPiDaemon(PID_FILE).stop()
    elif args.cmd == 'restart':
        DhtPiDaemon(PID_FILE).restart()
    else:
        print('error: Invalid cmd argument.', args.cmd)
        parser.print_help()
