from fastapi import FastAPI

from routers import url_shortener_router, users_router, authentication_router

app = FastAPI(title="URL Shortener API", description="API for URL Shortener", version="1.0.0")

app.include_router(url_shortener_router.router)
app.include_router(users_router.router, prefix="/api", tags=["users"])
app.include_router(authentication_router.router, tags=["authentication"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
