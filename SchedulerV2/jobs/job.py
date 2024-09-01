from abc import ABC, abstractmethod


class Job(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def get_next_run_time(self):
        pass
