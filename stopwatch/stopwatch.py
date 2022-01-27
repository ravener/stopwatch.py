"""
MIT License

Copyright (c) 2018 Free TNT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from __future__ import annotations

import time
from typing import Optional


# Ported from https://github.com/dirigeants/klasa/blob/541c9e5f5646db4162f54c7ed61362d479176eed/src/lib/util/Stopwatch.js
class Stopwatch:
    _start: float
    _end: Optional[float]

    def __init__(self):
        self._start = time.perf_counter()
        self._end = None

    @property
    def duration(self) -> float:
        """
        The duration of this stopwatch since start or start to end if this
        stopwatch has stopped.

        Returns:
            float: The duration of the stopwatch in seconds.

        """
        return (self._end or time.perf_counter()) - self._start

    @property
    def running(self) -> bool:
        """
        Check if the stopwatch is running or not.

        Returns:
            bool: True if the stopwatch is running, False if stopped.

        """
        return not self._end

    def restart(self) -> Stopwatch:
        """
        Reset and start the stopwatch.

        Returns:
            Stopwatch: The restarted stopwatch.

        """
        self._start = time.perf_counter()
        self._end = None
        return self

    def reset(self) -> Stopwatch:
        """
        Resets the Stopwatch to 0 duration.

        Returns:
            Stopwatch: The resetted stopwatch.
        
        """
        self._start = time.perf_counter()
        self._end = self._start
        return self

    def start(self) -> Stopwatch:
        """
        Starts the stopwatch.

        Returns:
            Stopwatch: The started stopwatch.

        """
        if not self.running:
            self._start = time.perf_counter() - self.duration
            self._end = None
        return self

    def stop(self) -> Stopwatch:
        """
        Stops the stopwatch, freezing the duration.

        Returns:
            Stopwatch: The stopped stopwatch.

        """
        if self.running:
            self._end = time.perf_counter()
        return self

    def __str__(self) -> str:
        time = self.duration * 1000
        if time >= 1000:
            return "{:.2f}s".format(time / 1000)
        if time >= 1:
            return "{:.2f}ms".format(time)
        return "{:.2f}μs".format(time * 1000)
