from abc import ABC, abstractmethod
import pickle
import time
import threading


class Scheduler(ABC):
    # Let's make use of a file to store the jobs
    def __init__(self, name):
        self.name = name
        self.job_queue = []
        self.registered_jobs = set()

    def start(self):
        while True:
            with open("job_queue.txt", "rb") as f:
                data = f.read()
                job = pickle.loads(data)
                print(self.registered_jobs)
                if job.get_id() not in self.registered_jobs:
                    self.registered_jobs.add(job.get_id())
                    self.job_queue.append(job)
            # 2 Run jobs
            # Jobs added to the job queue
            print("Tracking the following Jobs:")
            print(self.registered_jobs)
            self.run_jobs(job)
            time.sleep(5)

    def find_jobs(self):
        pass

    def run_jobs(self, job):
        threads = []
        for job in self.job_queue:
            if job.get_next_run_time() < time.time():
                thread = threading.Thread(target=job.run)
                threads.append(thread)
                job.set_next_run_time()

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        print("Jobs have been run")


if __name__ == "__main__":
    scheduler = Scheduler("MyScheduler")
    scheduler.start()
