# This file is placed in the Public Domain.


"a clean namespace"


import datetime
import os
import types
import uuid


from functools import wraps


def __dir__():
    return (
            'Object',
            'format',
            'items',
            'keys',
            'search',
            'update',
            'values'
            )


__all__ = __dir__()


class Object:

    def __init__(self, *args, **kwargs):
        ""
        if args:
            val = args[0]
            if isinstance(val, list):
                update(self, dict(val))
            elif isinstance(val, zip):
                update(self, dict(val))
            elif isinstance(val, dict):
                update(self, val)
            elif isinstance(val, Object):
                update(self, vars(val))
        if kwargs:
            self.__dict__.update(kwargs)

    def __iter__(self):
        ""
        return iter(self.__dict__)

    def __len__(self):
        ""
        return len(self.__dict__)

    def __oid__(self):
        ""
        return os.path.join(
                            self.__type__(),
                            str(uuid.uuid4().hex),
                            os.sep.join(str(datetime.datetime.now()).split()),
                           )

    def __str__(self):
        ""
        return str(self.__dict__)

    def __type__(self):
        ""
        kin = str(type(self)).split()[-1][1:-2]
        if kin == "type":
            kin = self.__name__
        return kin


def format(obj, args="", skip="", plain=False):
    res = []
    keyz = []
    if "," in args:
        keyz = args.split(",")
    if not keyz:
        keyz = keys(obj)
    for key in sorted(keyz):
        if key.startswith("_"):
            continue
        if skip:
            skips = skip.split(",")
            if key in skips:
                continue
        value = getattr(obj, key, None)
        if not value:
            continue
        if " object at " in str(value):
            continue
        txt = ""
        if plain:
            value = str(value)
            txt = f'{value}'
        elif isinstance(value, str) and len(value.split()) >= 2:
            txt = f'{key}="{value}"'
        else:
            txt = f'{key}={value}'
        res.append(txt)
    txt = " ".join(res)
    return txt.strip()


def items(obj):
    if isinstance(obj, type({})):
        return obj.items()
    return obj.__dict__.items()


def keys(obj):
    return obj.__dict__.keys()


def search(obj, selector):
    res = False
    select = Object(selector)
    for key, value in items(select):
        try:
            val = getattr(obj, key)
        except AttributeError:
            continue
        if str(value) in str(val):
            res = True
            break
    return res


def update(obj, data):
    for key, value in items(data):
        setattr(obj, key, value)


def values(obj):
    return obj.__dict__.values()
