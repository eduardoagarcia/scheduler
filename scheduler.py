#! /usr/bin/python

from datetime import datetime
import functools

# Create new scheduler class
class scheduler:

    # Init
    def __init__(self):

        # Now
        self._now = datetime.now()

        # Job variables
        self._job_func = None
        self._unit     = None
        self._time     = None
        self._value    = None

    # At
    def at(self, time):
        self._time = datetime.strptime(time, '%H:%M')
        return self

    # Every
    def every(self, value):
        self._value = value
        return self

    # Hours
    def hours(self):
        self._unit = self._now.hour
        return self

    # Minutes
    def minutes(self):
        self._unit = self._now.minute
        return self

    # Run check
    def runCheck(self):

        # Run at
        if (self._time):
            if ((self._time.hour == self._now.hour) and (self._time.minute == self._now.minute)):
                return True
            else:
                return False

        # Every x units
        if (self._value):
            if (self._unit % self._value == 0):
                return True
            else:
                return False

        # Run nothing
        return False

    # Do
    def do(self, method, *args, **kwargs):

        # Create our callable job function method
        self._job_func = functools.partial(method, *args, **kwargs)

        # Run the callable job function
        if ( self.runCheck() ):
            return self._job_func()

# eof