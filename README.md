[![CircleCI](https://circleci.com/gh/Olcina/udacity-devops/tree/master.svg?style=svg&circle-token=6a2453c97c754f0c3f980eb77ce43aa38f252917)](https://circleci.com/gh/Olcina/udacity-devops/tree/master)

# Prediction Api contenarized project
---

This project shows a way to contenarize a ML/AI workflow into a docker and a kubernetes enviroment.

# Setting up the project

## Setup the Environment

* Create a virtualenv and activate it
  To do this you can run `make setup`
* Run `make install` to install the necessary dependencies, and their correct versions, as described in the requirement.txt. For example, this command will install the supported version of scikit-learn `0.20.2`

### Running `app.py`

You have 3 options to run this project:

1. Standalone:  `python app.py`
2. Run in Docker:  `./run_docker.sh`
3. Run in Kubernetes:  `./run_kubernetes.sh`

Running this will set up the app running on the port provided by the scripts (5001).

In order to run the option 2 you need to install docker in your local machine. You can find more information about docker installation [here](https://docs.docker.com/install/)

For the option 3, a local kubernetes configuration is required. You can find more information about kubernetes installation [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/)