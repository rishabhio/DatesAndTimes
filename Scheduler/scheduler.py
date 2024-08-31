import time


class Job:
    def __init__(self, name):
        self.name = name
        self.next_run_time = time.time()

    def get_next_run_time(self):
        return self.next_run_time

    def run(self):
        print(f"Running job {self.name}")
        self.next_run_time = time.time() + 5


class Scheduler:
    def __init__(self):
        self.jobs = []

    def add_job(self, job):
        self.jobs.append(job)

    def run(self):
        for job in self.jobs:
            if job.get_next_run_time() < time.time():
                job.run()

    def remove_job(self, job):
        self.jobs.remove(job)


if __name__ == "__main__":
    scheduler = Scheduler()
    j1 = Job("Job 1")
    j2 = Job("Job 2")
    scheduler.add_job(j1)
    scheduler.add_job(j2)

    while True:
        try:
            time.sleep(1)
            scheduler.run()
        except KeyboardInterrupt:
            break
