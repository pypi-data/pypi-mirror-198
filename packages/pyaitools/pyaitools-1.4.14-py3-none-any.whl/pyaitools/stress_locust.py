import os
import math
from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape
from temp import request_body, time_limit, step_load, step_time, spawn_rate 



class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.request(**request_body)


class WebsiteUser(HttpUser):
    wait_time = constant(0.5)
    tasks = [UserTasks]



class StepLoadShape(LoadTestShape):
    """
    A step load shape
    Keyword arguments:
        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds
    """

    def tick(self):
        run_time = self.get_run_time()

        if run_time > time_limit:
            return None

        current_step = math.floor(run_time / step_time) + 1
        return (current_step * step_load, spawn_rate)
