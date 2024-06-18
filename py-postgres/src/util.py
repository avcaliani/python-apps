from time import time


class Timer:

    def __init__(self):
        self.started_at = time()

    def stop(self):
        seconds = round(time() - self.started_at, 2)
        if seconds < 60:
            return f'{seconds}s'

        minutes = round(seconds / 60, 2)
        if minutes < 60:
            return f'{minutes}m'

        return f'{round(minutes / 60, 2)}h'
