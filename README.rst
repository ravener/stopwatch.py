Stopwatch.py
============
A simple stopwatch for Python that is small, efficient and requires no dependencies.

Install
-------

.. code:: sh

   pip install stopwatch.py

Usage
-----
.. code:: py

    from stopwatch import Stopwatch

    stopwatch = Stopwatch() # Stopwatch keeps running
    # but really its just math with time.perf_counter() so there isn't really a task
    # running in background

    stopwatch.stop() # stop stopwatch, time freezes
    stopwatch.start() # Start it again
    stopwatch.reset() # reset it back to 0
    stopwatch.restart() # reset and start again
    stopwatch.running # wether stopwatch is running
    stopwatch.duration # Get the duration
    str(stopwatch) # Get the friendly duration string


Python2 Support?
----------------
Sorry, this module depends on ``time.perf_counter()`` which doesn't exist on Python2. However, it should be compatible with any python3+ versions, maybe even other python implementations if it implements ``time.perf_counter()``

License
-------
MIT

Credits
-------
Originally written by `dirigeants <https://github.com/dirigeants>`_ in `this file <https://github.com/dirigeants/klasa/blob/541c9e5f5646db4162f54c7ed61362d479176eed/src/lib/util/Stopwatch.js>`_ i just looked at it and rewrote it in python, and it felt useful to put it in a module.
