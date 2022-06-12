Stopwatch.py
============
A simple stopwatch for python, small, efficient and no dependencies

Install
-------
Requires Python 3+ since this module depends on ``time.perf_counter()`` which does not exist in Python 2.

.. code:: sh

   pip install stopwatch.py

Usage
-----
.. code:: py

    from stopwatch import Stopwatch

    # Argument specifies decimal precision for __str__
    # e.g 2 digits = 1.00, 3 digits = 1.000
    # Optional, defaults to 2
    stopwatch = Stopwatch(2) # Start a stopwatch
    # It's just math with time.perf_counter() so there isn't really a task
    # running in background

    stopwatch.stop() # Stop stopwatch, time freezes
    stopwatch.start() # Start it again
    stopwatch.reset() # Reset it back to 0
    stopwatch.restart() # Reset and start again
    stopwatch.running # Wether stopwatch is running
    stopwatch.duration # Get the duration (in seconds)
    str(stopwatch) # Get a friendly duration string

License
-------
MIT

Credits
-------
Originally written by `dirigeants <https://github.com/dirigeants>`_ in `this file <https://github.com/dirigeants/klasa/blob/master/src/lib/util/Stopwatch.js>`_ i just looked at it and rewrote it in python, and it felt useful to put it in a module.
