import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from stopwatch import Stopwatch
import asyncio
import time
import unittest


class StopwatchTest(unittest.TestCase):
    def testStopwatch(self):
        """Tests stopwatch timing"""
        stopwatch = Stopwatch()
        time.sleep(0.1)
        stopwatch.stop()

        # Can't gurantee exact timings as python speed may differ each execution
        # so ensure it is atleast a 100ms
        # also a test for the friendly time string
        self.assertTrue(stopwatch.duration >= 0.1)
        self.assertTrue(str(stopwatch).endswith("ms"))

        stopwatch.start()
        time.sleep(1)
        stopwatch.stop()

        self.assertTrue(stopwatch.duration >= 1.1)
        self.assertTrue(str(stopwatch).endswith("s"))

    def testStop(self):
        """Tests stopwatch's stopped state"""
        stopwatch = Stopwatch()
        stopwatch.stop()

        now = str(stopwatch)
        time.sleep(0.1)
        after = str(stopwatch)

        # A stopped stopwatch should not move
        self.assertEqual(now, after)

    def testRunning(self):
        """Tests that the running boolean works as expected"""
        stopwatch = Stopwatch()
        self.assertTrue(stopwatch.running)

        stopwatch.stop()
        self.assertFalse(stopwatch.running)

        stopwatch.restart()
        self.assertTrue(stopwatch.running)

    def testDigits(self):
        """Tests that the string contains the correct precision"""
        stopwatch = Stopwatch(4)
        time.sleep(1)
        stopwatch.stop()

        # e.g 5.7282s
        self.assertTrue(len(str(stopwatch)) == 7)

    def testDuration(self):
        """Tests that the duration results works as expected"""
        stopwatch = Stopwatch()
        time.sleep(1)
        stopwatch.stop()

        self.assertTrue(stopwatch.duration >= 1)

    def testAsync(self):
        """Tests that it doesn't do any bad behaviors on asyncio event loop"""

        async def main():
            stopwatch = Stopwatch()
            await asyncio.sleep(1)
            stopwatch.stop()

            self.assertTrue(stopwatch.duration >= 1)

        asyncio.run(main())


if __name__ == "__main__":
    unittest.main()
