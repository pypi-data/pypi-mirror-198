import time
from copy import copy
from typing import Optional, List
from ..domain.repository import TaskQueueRepository, TaskProcessRepository


class CacheQueue:
    def __init__(self) -> None:
        self.cache = {}
        self.queue = None


    def _next(self):
        while True:
            index = next(self.queue)
            if index in self.cache:
                return index
    

    def _pop(self):
        if self.queue is None:
            self.queue = iter(copy(self.cache))
        try:
            return self.cache[self._next()]
        except StopIteration:
            self.queue = iter(copy(self.cache))
            return None
    

    def _pop_index(self):
        if self.queue is None:
            self.queue = iter(copy(self.cache))
        try:
            return self._next()
        except StopIteration:
            self.queue = iter(copy(self.cache))
            return None
    
    
    def delete(self, index)->bool:
        if index in self.cache:
            del self.cache[index]
            return True
        else:
            return False
    

class SimpleTaskProcessor:
    def __init__(
        self, 
        queue_repo:TaskQueueRepository, 
        process_repo: TaskProcessRepository,
        delay:int = 1
    ) -> None:
        self.queue_repo = queue_repo
        self.process_repo = process_repo
        self.delay = delay
    

    def set_queue_repo(self, queue_repo: TaskQueueRepository):
        self.queue_repo = queue_repo
    

    def set_process_repo(self, process_repo: TaskProcessRepository):
        self.process_repo = process_repo


    def gen_item(self, request):
        raise NotImplementedError


    def get_task(self, queue_repo: Optional[TaskQueueRepository]=None):
        queue_repo = queue_repo or self.queue_repo
        return queue_repo.get_task()
    

    def get_tasks(self, queue_repo: Optional[TaskQueueRepository]=None, n=10):
        queue_repo = queue_repo or self.queue_repo
        return queue_repo.get_n_tasks(n)
    

    def process_task(self, item, process_repo:Optional[TaskProcessRepository]=None):
        process_repo = process_repo or self.process_repo
        return process_repo.process(item)
    

    def process_tasks(self, items, process_repo:Optional[TaskProcessRepository]=None):
        if process_repo is None:
            process_repo = self.process_repo
        return process_repo.process_batch(items)

    
    def save_item(self, item, queue_repo: Optional[TaskQueueRepository]=None)->bool:
        queue_repo = queue_repo or self.queue_repo
        return queue_repo.save_item(item)
    

    def save_items(self, items, queue_repo: Optional[TaskQueueRepository]=None)->List[bool]:
        queue_repo = queue_repo or self.queue_repo
        return queue_repo.save_items(items)
    

    def process_when_failed(self, item):
        # log or warning by email
        raise NotImplementedError
    

    def process_when_failed_batch(self, items):
        raise NotImplementedError
    

    def postprocess(self, item, process_repo:Optional[TaskProcessRepository]=None)->bool:
        return True, item
    

    def postprocess_batch(
        self, 
        items, 
        process_repo:Optional[TaskProcessRepository]=None
    )->List[bool]:
        return [True]*len(items), items


    def preprocess(self, item, process_repo:Optional[TaskProcessRepository]=None):
        return True, item
    

    def preprocess_batch(
        self, 
        items, 
        process_repo:Optional[TaskProcessRepository]=None
    )->List[bool]:
        return [True]*len(items), items
    

    def run(
        self, 
        queue_repo: Optional[TaskQueueRepository]=None, 
        process_repo: Optional[TaskProcessRepository]=None,
        delay=None, 
        n_loop=1000000000
    ):
        queue_repo = queue_repo or self.queue_repo
        process_repo = process_repo or self.process_repo
        delay = delay or self.delay
        for i in range(n_loop):
            time.sleep(delay)
            request = self.get_task(queue_repo)
            if not request:
                continue

            # generate item
            item = self.gen_item(request)
            succeed = self.save_item(item)
            if not succeed:
                self.process_when_failed(item)

            # preprocess
            succeed, item = self.preprocess(item, process_repo)
            if not succeed:
                self.process_when_failed(item)

            # process
            item = process_repo.process(item)
            succeed = self.save_item(item)
            if not succeed:
                self.process_when_failed(item)

            # postprocess
            succeed, item = self.postprocess(item, process_repo)
            if not succeed:
                self.process_when_failed(item)

