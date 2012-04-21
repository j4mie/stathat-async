# -*- coding: utf-8 -*-

"""
stathat-async

A simple multiprocessing-based async wrapper around Kenneth Reitz's stathat.py

Usage:

    >>> from stathatasync import StatHat
    >>> stats = StatHat('email@example.com')
    >>> stats.count('wtfs/minute', 10)
    >>> stats.value('connections.active', 85092)

The calls to count and value won't block your program while the HTTP
request to the StatHat API is made. Instead, the requests will be made in a
subprocess.

Enjoy!

"""

import multiprocessing
import stathat


class StatHatWorker(multiprocessing.Process):

    def __init__(self, email, queue):
        super(StatHatWorker, self).__init__()
        self.queue = queue
        self.stathat = stathat.StatHat(email)

    def run(self):
        while True:
            command, key, value = self.queue.get()

            if command == 'value':
                self.stathat.value(key, value)
            if command == 'count':
                self.stathat.count(key, value)


class StatHat(object):

    def __init__(self, email):
        self.queue = multiprocessing.Queue()
        worker = StatHatWorker(email, self.queue)
        worker.start()

    def value(self, key, value):
        self.queue.put(('value', key, value))

    def count(self, key, count):
        self.queue.put(('count', key, count))
