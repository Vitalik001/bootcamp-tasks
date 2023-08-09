from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foolock = Lock()
        self.barlock = Lock()
        self.barlock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.foolock.acquire()
            printFoo()
            self.barlock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.barlock.acquire()
            printBar()
            self.foolock.release()
