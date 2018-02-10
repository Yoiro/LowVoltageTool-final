#!/usr/bin/env python
# coding=utf-8


"""Contains classes Observer and Observable"""


class Observer:
    """Implementation of the Observer Pattern."""
    def update(self):
        pass


class Observable:
    """Implementation of the Observer Pattern (Observable)."""
    def __init__(self):
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)
