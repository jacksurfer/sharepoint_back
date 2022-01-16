# sharepoint_back

## Build Setup

```bash

# Clone project
$ git clone https://github.com/jacksurfer/sharepoint_back.git

# Install Poetry
$ pip install poetry

# Activating the virtual environment
$ poetry shell

# install dependencies
$ poetry install

# serve with hot reload at localhost:8000
$ make run
or
$ uvicorn app.main:app --reload

```


```bash

# config.py
site_url = "https://****.sharepoint.com"
client_id = "4dc68f28-****-****-****-456354f0d4a2"
client_secret = "*********************************"

```