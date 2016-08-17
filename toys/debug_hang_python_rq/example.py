# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import time

from rq import Connection, Queue

from .fib import slow_fib


def main():
    q = Queue()
    q.enqueue(slow_fib, 50)


if __name__ == '__main__':
    # Tell RQ what Redis connection to use
    with Connection():
        main()
