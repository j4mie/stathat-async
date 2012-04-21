# stathat-async

A simple multithreaded async wrapper around Kenneth Reitz's
[stathat.py](https://github.com/kennethreitz/stathat.py)

## Usage

    >>> from stathatasync import StatHat
    >>> stats = StatHat('email@example.com')
    >>> stats.count('wtfs/minute', 10)
    >>> stats.value('connections.active', 85092)

The calls to `count` and `value` won't block your program while the HTTP
request to the StatHat API is made. Instead, the requests will be made in a
separate thread.

Enjoy!

## Installation

Installation is simple::

    $ pip install stathat-async
