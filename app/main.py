from typing import Union
import socket 
import os
import uvicorn
import psutil
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    sys_user = os.getenv('USER')
    # Getting loadover15 minutes
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage = (load15/os.cpu_count()) * 100
    return {"Hello": "k8s", 'hostname': hostname, 'ipaddress': ipaddress, 'user': sys_user, 'cpu_usage': f'{cpu_usage:.2f}%'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
