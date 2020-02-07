from locust import HttpLocust, TaskSet, between



def index(l):
    l.client.get("/")

def predict(l):
    l.client.post("/predict",json={
      "CHAS":{ "0":0 },
      "RM":{ "0":6.575},
      "TAX":{  "0":296.0},
      "PTRATIO":{"0":15.3},
      "B":{"0":396.9},
      "LSTAT":{"0":4.98}
    })

class UserBehavior(TaskSet):
    tasks = {index: 1, predict: 1}

    # def on_start(self):
    #     index(self)
    #     predict(self)
    #     # login(self)

    # def on_stop(self):
    #     logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)