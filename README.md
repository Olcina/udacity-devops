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

NOTE: make sure to update the `dockerpath` to your account docker path

Running this will set up the app running on the port provided by the scripts (5001).

In order to run the option 2 you need to install docker in your local machine. You can find more information about docker installation [here](https://docs.docker.com/install/)

For the option 3, a local kubernetes configuration is required. You can find more information about kubernetes installation [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

# Files description

- app.py: contains the application logic, spins up a flask web server that handles the http request to our ML algorithm
- DockerFile: detailed instruction so that docker can build an enviroment to run `app.py`
- make_prediction.sh: a shell script that makes a curl call to our running web server
- Makefile: contains automations for our shell scrips and commands
- README.md: You are reading it!
- requirements.txt: describe the necessary python modules to intall in our python environment
- run_docker.sh: build and run the project in a docker container
- run_kubernetes.sh: spins a kubernete pod from the docker image defined in `dockerpath`
