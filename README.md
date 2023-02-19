# DisCTFd

Automation CTFd platform with bot discord, notify first blood or just solved challenge, and get a info data from your host CTFd platform

## How To Run?

### 1. Clone this repo

```bash
git clone https://github.com/ardhptr21/DisCTFd.git
```

### 2. Install requirements

```bash
$ pip install -r requirements.txt

# or

$ pip3 install -r requirements.txt
```

### 3. Change the config

Change the config in `config.py` file, and fill the config with your data

> NOTE: **Webhook** is for notify the first blood/solved challenge, and **Bot** is for get a info data from your host CTFd platform

### 4. Run

#### 4.1. Run with python

```bash
$ python main.py

# or

$ python3 main.py
```

#### 4.2. Run with docker

```bash
# without docker compose
$ docker build -t disctfd .
$ docker run -d --name disctfd disctfd

# with docker compose
$ docker-compose up -d
```
