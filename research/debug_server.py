from fastapi import FastAPI, Request

app = FastAPI()

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def catch_all(path: str, request: Request):
    # Extract method, path, and body from the request
    method = request.method
    
    try:
        body = await request.json()
    except:
        body = {}

    print(f"Method: {method}")
    print(f"Path: /{path}")
    print(f"Body: {body}")

    return {"message": "Request captured!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
