# -*- coding: UTF-8 -*-
"""
A debugger for running process.

link:
    http://stackoverflow.com/questions/132058/showing-the-stack-trace-from-a-running-python-application
"""
from __future__ import print_function

import traceback
import signal
import logging


class Debugger(object):

    def __init__(self, handler=None):
        self.handler = handler

    def signal_handler(self, sig, frame):
        self.handler(frame)


def debug_handler(frame):
    message = 'Traceback:\n' + ''.join(traceback.format_stack(frame))
    print(message)


def debug_on_signal(sig, handler=debug_handler):
    debugger = Debugger(handler=handler)
    signal.signal(sig, debugger.signal_handler)  # Register handler
