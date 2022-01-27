from stopwatch import Stopwatch
import asyncio
import time
import unittest

# Testing various functions to check if it works as expected
# To run this you will need python3.5+ due to async/await usage
# To make it compatible with python3.4 change the
# `async def` to a
# @asyncio.coroutine
# def stuff():
#     ...
# and the `await` to a `yield from`
# For even lower python versions where asyncio didn't exist, just comment
# that lines


class StopwatchTest(unittest.TestCase):

    def testStopwatch(self):
        """Tests stopwatch timing"""
        stopwatch = Stopwatch()
        time.sleep(0.1)
        stopwatch.stop()
        m = str(stopwatch)

        # Can't guarantee exact timings as python speed may differ each
        # execution so ensure it is at least a 100ms
        # also a test for friendly time string
        self.assertTrue(m.startswith("100") and m.endswith("ms"))

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

    def testDuration(self):
        """Tests that the duration results works as expected"""
        stopwatch = Stopwatch()
        time.sleep(1)
        stopwatch.stop()
        duration = stopwatch.duration * 1000
        self.assertTrue(duration >= 1000)

    def testAsync(self):
        """Tests that it doesn't do any bad behaviors on asyncio event loop"""

        async def main():
            stopwatch = Stopwatch()
            await asyncio.sleep(1)
            self.assertTrue((stopwatch.duration * 1000) >= 1000)

        asyncio.get_event_loop().run_until_complete(main())


if __name__ == "__main__":
    unittest.main()
