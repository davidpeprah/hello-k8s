from typing import Union
import socket uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    return {"Hello": "k8s", 'hostname': hostname, 'ipaddress': ipaddress}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
