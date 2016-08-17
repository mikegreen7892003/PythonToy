# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import signal

from rq import Connection, Queue, Worker
from tornado.options import parse_command_line

from .debug import debug_on_signal


if __name__ == '__main__':
    parse_command_line()

    debug_on_signal(signal.SIGUSR1)

    # Tell rq what Redis connection to use
    with Connection():
        q = Queue()
        Worker(q).work()
