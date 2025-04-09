# Mini-Rag

This is a minimal implementation of the RAG model for question answering.

## Requirements 

- Python 3.8 or later

### Install Python using MininConda 

1) Download and install MiniConda from [here](https://www.anaconda.com/docs/main#quick-command-line-install) 
2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8
```
3) Activate the environment:
```bash
$ conda activate mini-rag
```
### (Optional) Setup you command line interface for better readability
```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```
### setup the environment variable 

```bash
$ cp .env.example .env
```

Set your environment variable in the '.env' file. Like
'OPENAI_API_KEY' value.

### Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0
```
