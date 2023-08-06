from abc import ABC
from typing import Callable, NoReturn, Any, Sequence
from inspect import getfullargspec



class Trigger(ABC):
    def __init__(self):
        self.listeners = []
    listeners: list[Callable[[dict[str, Any]], NoReturn]]


def chain(trigger: Trigger, *args: Callable):
    def listener(context: dict[str, Any]):
        current_arg: Any = None
        for function in args:
            a = getfullargspec(function)
            if current_arg is None or len(a.args) == 0:
                if a.varkw is None:
                    current_arg = function()
                else:
                    current_arg = function(context=context)
            else:
                if a.varkw is None:
                    current_arg = function(current_arg)
                else:
                    current_arg = function(current_arg, context=context)
    trigger.listeners.append(listener)