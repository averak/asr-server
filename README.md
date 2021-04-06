# asr-server

[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

ASR (Automatic Speech Recognition) Server

## Requirement

- Python 3.8
- pipenv

## Installation

```sh
$ git clone <this repo>
$ cd <this repo>

$ pipenv install
```

## Usage

### 1. Create Data

```sh
$ pipenv run record
# You need to record the speech you want to recognize
$ pipenv run build
```

### 2. Training

```sh
$ pipenv run train
```

### 3. Start ASR Server

```sh
$ pipenv run start
```

### 4. Start Demo app

When the demo-app starts, please speak a voice. The server will recognize it.

```sh
$ pipenv run demo
```

