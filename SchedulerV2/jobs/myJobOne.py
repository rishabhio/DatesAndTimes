from jobs.job import Job
import time
import pickle


class MyJobOne(Job):
    def __init__(self):
        self.next_run_time = time.time() + 10
        self.interval = 10
        self.one_time = False

    def get_id(self):
        return "MyJobOne"

    def run(self):
        print("Running MyJobOne")

    def get_next_run_time(self):
        return self.next_run_time

    def set_next_run_time(self):
        self.next_run_time = time.time() + self.interval
