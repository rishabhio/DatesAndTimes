from jobs import myJobOne
import pickle
import time


if __name__ == "__main__":
    job = myJobOne.MyJobOne()
    serialized = pickle.dumps(job)
    with open("job_queue.txt", "wb") as f:
        f.write(serialized)
