from typing import Union
import socket 
import os, sys
import uvicorn
import psutil
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    sys_platform = sys.platform
    cpu_percent = psutil.cpu_percent()
    return {"Hello": "k8s", 'hostname': hostname, 'ipaddress': ipaddress, 'system': sys_platform, 'cpu_usage': f'{cpu_percent:.2f}%'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
