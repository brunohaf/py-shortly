from typing import Union

from fastapi import FastAPI

from routers import url_shortener_router, users_router

app = FastAPI(root_path="/api", title="URL Shortener API", description="API for URL Shortener", version="1.0.0")

app.include_router(url_shortener_router.router)
app.include_router(users_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
