import os
import uvicorn
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(title="ConnectSphere AI API")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "ConnectSphere AI API"}

# Health check endpoint
# @app.get("/health")
# async def health_check():
#     return {"status": "healthy"}

# Example API endpoint
@app.get("/api/hello/{name}")
async def hello(name: str):
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        reload=True
    )