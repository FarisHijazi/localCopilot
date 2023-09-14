from fastapi import FastAPI, Request
import datetime
import os
import json
import time

# import curlify
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

global logs_path

app = FastAPI(middleware=[Middleware(CORSMiddleware, allow_origins=["*"])])


@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def catch_all(path: str, request: Request):
    # Extract method, path, and body from the request
    method = request.method

    try:
        body = await request.json()
    except:
        body = {}

    global logs_path

    with open(logs_path, "a") as f:
        print(
            json.dumps(
                {
                    "timestamp": time.time(),
                    "path:": "http://localhost:5001" + path,
                    "method": method,
                    "body": body,
                },
                indent=4,
            ),
            file=f,
        )
        # print(curlify.to_curl(request), file=f)
        # print(to_curl(request))
        # print(curl_request(path, method, headers=request.headers, payloads=body))
    return {"message": "Request captured!"}


if __name__ == "__main__":
    import uvicorn

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
    os.makedirs("./logs", exist_ok=True)
    logs_path = f"./logs/{timestamp}.log"
    with open(logs_path, "w") as f:
        print("", file=f, end="")
    print("outputting to file:", logs_path)

    uvicorn.run(app, host="0.0.0.0", port=5000)

#
