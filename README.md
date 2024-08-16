# Flask Data Processing Application

This is a simple Flask application that simulates data retrieval from an external service, processes the data, and
stores the result in memory. It also provides endpoints to fetch and retrieve processed data.

## Features

1. **Data Retrieval**: Simulates fetching data from an external service.
2. **Data Processing**: Converts text to uppercase and sums a series of numbers.
3. **Data Storage**: Stores processed data in temporary in-memory storage.
4. **Data Retrieval Endpoint**: Provides an endpoint to get the processed data.

## Setup and Running Locally

### Prerequisites

- Python 3.8 or higher
- sudo pip install virtualenvwrapper

## How to Setup Development Enviornment

There are 2 steps to set this up locally.
Step 1: Prepare your machine with system level packages
Step 2: Setup project, including Python dependencies.

### Step 1: Prepare your machine with system level packages

Please run following commands on your terminal (ubuntu os only).
```
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev

#For Python 3.8, To Update to python3.8 run following commands
sudo apt-get install python3.8-dev default-libmysqlclient-dev

#Install other dependencies:
sudo apt-get install gcc libssl-dev
```

### Step 2: Project Setup on Local

1. Run below commands on your machine to generate SSH key.
```
ssh key-gen
cd ~/.ssh
cat id_rsa.pub
```
2. Copy your key from the terminal and go to SSH and CPG keys and upload your ssh key.

3. Clone project repository from code commit
```commandline
git clone git@github.com:ankur0103/data-retrieval-system.git
```
4. Set git configuration, add username and email for the current repository
```commandline
git config user.name xxx
git config user.email yyy
```

5. For first time setup, Make virtual env `mkvirtualenv data-retrieval`
    ```
    To exit virtual environment: type command 'deactivate'
    For going back to virtual environment: type command 'workon data-retrieval'
    ```
   
6. Install required python packages
   `pip install -r requirements.txt`

7. cd data-retrieval-system

8. To run the flask server, run below command on terminal
    `flask run` or `python app.py`