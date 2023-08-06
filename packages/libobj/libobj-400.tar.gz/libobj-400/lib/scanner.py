# This file is placed in the Public Domain.


"introspection"


import importlib
import inspect
import os


from command import Command
from storage import Storage
from utility import spl


def __dir__():
    return (
            'importer',
            'initer',
            'scan',
            'scandir',
            'scanpkg'
           )


def doimport(name, path):
    mod = None
    spec = importlib.util.spec_from_file_location(name, path)
    if spec:
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    return mod


def include(txt, vals):
    for val in vals:
        if val in txt:
            return True
    return False


def importer(name, path):
    mod = doimport(name, path)
    scan(mod)
    return mod


def initer(mname, path=None):
    mod = doimport(mname, path)
    if "start" in dir(mod):
        mod.start()
    return mod


def listmods(path):
    return sorted([x[:-3] for x in os.listdir(path) if not x.startswith("__")])


def scan(mod):
    scancls(mod)
    for key, cmd in inspect.getmembers(mod, inspect.isfunction):
        if key.startswith("cb"):
            continue
        names = cmd.__code__.co_varnames
        if "event" in names:
            Command.add(cmd.__name__, cmd)


def scancls(mod):
    for _key, clz in inspect.getmembers(mod, inspect.isclass):
        Storage.add(clz)


def scanpkg(pkg, func, mods=None):
    path = pkg.__path__[0]
    return scandir(path, func, mods)        


def scandir(path, func, mods=None, all=False):
    if mods is None:
        mods = []
    else:
        mods = spl(mods)
    res = []
    if not os.path.exists(path):
        return res
    for fnm in os.listdir(path):
        if fnm.endswith("~") or fnm.startswith("__"):
            continue
        if not all and not include(fnm, mods):
            continue                
        mname = fnm.split(os.sep)[-1][:-3]
        path2 = os.path.join(path, fnm)
        res.append(func(mname, path2))
    return res
