"""
Implements basic thread pool compatible with the standard THreadPoolExecutor, but with extra features and optimizing
performance.
"""
import logging
import queue
import threading
from typing import Callable


logger = logging.getLogger('glored-threadpool')


class FastThreadPoolExecutor:
    def __init__(self, max_workers=5, thread_name_prefix='', max_size: int = 1000):
        self._num_workers = max_workers
        self._max_size = max_size
        self.thread_name_prefix = thread_name_prefix
        self._job_queue = queue.SimpleQueue()
        self._workers = [threading.Thread(target=self._target, daemon=True, name=f'{thread_name_prefix}_{i}')
                         for i in range(self._num_workers)]
        for worker in self._workers:
            worker.start()

    def _target(self):
        while True:
            func, args, kwargs = self._job_queue.get()
            func(*args, **kwargs)

    def submit(self, func: Callable, /, *args, **kwargs):
        """
        Submits a job to the pool.
        """
        if self._job_queue.qsize() > self._max_size:
            logger.warning('Job queue is full, discarding message. You might want to increase the number of workers to '
                           'avoid this issue.')
        self._job_queue.put((func, args, kwargs))
