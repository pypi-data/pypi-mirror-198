README
######

**NAME**

|
| ``libobj`` - object library
|

**SYNOPSIS**


The ``libobj`` library provides an Object class, that allows for save/load 
to/from json files on disk. Objects can be searched with database functions
and have a  type in filename for reconstruction. Methods are factored out
into functions to have a clean namespace to read JSON data into.

|

**INSTALL**

|
| ``python3 -m pip install libobj``
|

**PROGRAMMING**

basic usage is this::

 >>> from objects import Object
 >>> o = Object()
 >>> o.key = "value"
 >>> o.key
 >>> 'value'

Objects try to mimic a dictionary while trying to be an object with normal
attribute access as well. hidden methods are provided, the methods are
factored out into functions like get, items, keys, register, set, update
and values.

load/save from/to disk::

 >>> from objects import Object
 >>> from storage import read, save
 >>> o = Object()
 >>> o.bla = "mekker"
 >>> p = save(o)
 >>> oo = Object()
 >>> read(oo, p)
 <objects.Object object at 0x7f98e57c4be0>
 >>> print(oo)
 {'bla': 'mekker'}
 >>> 

great for giving objects peristence by having their state stored in files.

|

**AUTHOR**

|
| Bart Thate <bthate@dds.nl>
|

**COPYRIGHT**

|
| ``libobj`` is placed in the Public Domain.
|
