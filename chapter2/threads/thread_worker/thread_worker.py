from threading import Thread


class ThreadWorker(Thread):
    def __init__(self):
        """Our workers constructor"""

        super(ThreadWorker, self).__init__()

    def run(self):
        for i in range(10):
           print(i)
