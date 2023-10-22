import threading


class ThreadWithResult(threading.Thread):
    def __init__(
        self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None
    ):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        super().join()
        return self._return


if __name__ == "__main__":

    def test_fun(start, end):
        summation = 0
        for i in range(start, end):
            summation += i

        return summation

    t1 = ThreadWithResult(target=test_fun, args=(1, 10))
    t2 = ThreadWithResult(target=test_fun, args=(1, 20))

    t1.start()
    t2.start()

    t1 = t1.join()
    t2 = t2.join()

    print(t1)
    print(t2)
