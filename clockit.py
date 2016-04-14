import functools
import timeit


class Clocked(object):
    """Container for metadata about the timed function.

    Arguments:
        result: The result returned by the timed function.
        timings (list): The list of results returned by calling timeit.repeat()
    """
    def __init__(self, result, timings):
        self.result = result
        self.timings = timings

    @property
    def time(self):
        # https://docs.python.org/3/library/timeit.html#timeit.Timer.repeat
        return min(self.timings)


def clockit(function, *args, executions=1000, repeat=3, **kwargs):
    """Time the execution of a function with the provided arguments.

    Returns:
        float, time required to run the function `executions` times.
    """
    nullary = functools.partial(function, *args, **kwargs)

    result = nullary()
    timings = timeit.repeat(nullary, number=executions, repeat=repeat)

    # TODO: Initialize Clocked with nullary, use a method to do the timing
    # done above and store results on the class.
    clocked = Clocked(result, timings)

    return clocked
