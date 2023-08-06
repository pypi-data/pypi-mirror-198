# This file is placed in the Public Domain.


'command'


import inspect
import _thread


from .objects import Object
from .message import Message
from .threads import threaded
from .utility import locked


def __dir__():
    return (
            'Command',
            'scan'
           )

execlock = _thread.allocate_lock()


class Command(Object):

    cmds = Object()

    @staticmethod
    def add(cmd, func):
        setattr(Command.cmds, cmd, func)

    @staticmethod
    def handle(evt):
        evt.parse(evt.txt)
        func = getattr(Command.cmds, evt.cmd, None)
        if func:
            func(evt)
            evt.show()
        return evt


def command(cli, txt):
    evt = cli.event(txt)
    Command.handle(evt)
    evt.ready()
    return evt


def scan(mod):
    for _key, cmd in inspect.getmembers(mod, inspect.isfunction):
        if 'event' in cmd.__code__.co_varnames:
            Command.add(cmd.__name__, cmd)
