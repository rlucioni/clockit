import functools
import timeit


def clockit(function, *args, executions=1000, repeat=3, **kwargs):
    """Time the execution of a function with the provided arguments.

    Returns:
        float, time required to run the function `executions` times.
    """

    # Turn a function with arguments into a function without arguments.
    nullary = functools.partial(function, *args, **kwargs)

    # https://docs.python.org/3/library/timeit.html#timeit.Timer.repeat
    best_time = min(timeit.repeat(nullary, number=executions, repeat=repeat))

    # TODO: Return an object containing the result of running the function
    # and metadata about the timing (e.g., executions, repeat).
    return best_time
