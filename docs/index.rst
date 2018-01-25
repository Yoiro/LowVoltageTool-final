.. Low Voltage Tool documentation master file, created by
   sphinx-quickstart on Thu Jan 18 21:36:29 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
============================================
Welcome to Low Voltage Tool's documentation!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Models
======
Models contains the classes that defines all the behaviours of an Electrical Network based on GELE's analysis.
.. automodule:: app.models

Serialization
=============
Serialization classes are meant to persist datas (basically to load/save some backend-network or GUI-network)
.. automodule:: app.serialization

WXViews
=======
WXViews contains all the implementation of the GUI that the Low Voltage Tool requires.
.. automodule:: app.wxviews

Core
----
Here lies the main modules used for the GUI development.
.. automodule:: app.wxviews.core

Panels
------
The panels are just the main components of the window, containing every single graphical item.
.. automodule:: app.wxviews.panels

Table
-----
The modules here are used to implement the Tabs, Grids, Tables, used on the right side of the GUI.
.. automodule:: app.wxviews.panels.table

Items
-----
Represents the Graphical representation of the Models items. Those are meant to contain both one model-class attribute and the state of its GUI representation
.. automodule:: app.wxviews.items

Drawers
-------
Classes used to tell the tool how to draw those items
.. automodule:: app.wxviews.drawers

Patterns
--------
Design Patterns in the most Pythonic Java way and being the most comprehensive possible for people coming from the JAVA world.
.. automodule:: app.wxviews.patterns


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


