"""Tool for timing the execution of Python functions."""
import functools
import timeit


class Clocked(object):
    """Utility class for timing the execution of a function.

    Initialization requires a function callable without arguments. The
    function is run `executions` times, repeated `repetitions` times.
    `executions` defaults to 1000, and `repetitions` to 3, resulting in 3 runs
    of 1000 executions each. The shortest of these times is reported as the
    function's execution time.

    Arguments:
        nullary (function): Function without arguments to time.

    Keyword Arguments:
        executions (int): Number of times to execute the provided function.
        repetitions (int): Number of times to repeat executions of the
            provided function.
    """
    def __init__(self, nullary, executions=1000, repetitions=3):
        self.nullary = nullary
        self.executions = executions
        self.repetitions = repetitions

        self.result = None
        self.timings = None

    @property
    def run(self):
        """Time the provided function, storing its return value."""
        self.result = self.nullary()
        self.timings = timeit.repeat(
            self.nullary,
            number=self.executions,
            repeat=self.repetitions
        )

    @property
    def time(self):
        """Give a lower bound for how fast the provided function can be run.

        For more details on this approach, see
        https://docs.python.org/3/library/timeit.html#timeit.Timer.repeat.
        """
        return min(self.timings)


def clockit(function, *args, executions=1000, repetitions=3, **kwargs):
    """Time the execution of a function with the provided arguments.

    Arguments:
        function (function): Function to time.
        args: Any number of positional arguments with which to call the
            provided function.

    Keyword Arguments:
        executions (int): Number of times to execute the provided function.
        repetitions (int): Number of times to repeat executions of the
            provided function.
        kwargs: Any number of keyword arguments with which to call the
            provided function.

    Returns:
        Clocked, containing shortest time required to run the function
        `executions` times.
    """
    nullary = functools.partial(function, *args, **kwargs)
    clocked = Clocked(
        nullary,
        executions=executions,
        repetitions=repetitions
    )

    clocked.run

    return clocked
