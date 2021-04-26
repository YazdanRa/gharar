class Backoff(object):
    def get_delay_amount(self, retry_number):
        raise NotImplementedError()


class ExponentialBackoff(Backoff):
    def __init__(self, starting_delay, time_multiple):
        self._starting_delay = starting_delay
        self._time_multiple = time_multiple

    def get_delay_amount(self, retry_number):
        return self._starting_delay * self._time_multiple ** retry_number


class LinearBackoff(Backoff):
    def __init__(self, starting_delay, time_addition):
        self._starting_delay = starting_delay
        self._time_addition = time_addition

    def get_delay_amount(self, retry_number):
        return self._starting_delay + self._time_addition * retry_number
