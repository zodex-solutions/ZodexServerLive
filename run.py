import os
import uvicorn

from app.config import APP_HOST, APP_PORT, STATIC_DIR
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from server import app

# ✅ CORS configuration
origins = [
    "http://localhost:3000",  
    "http://127.0.0.1:3000",
    "https://zodex.in",
    # Add your production frontend URL here
    # "https://yourdomain.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # allowed origins
    allow_credentials=True,
    allow_methods=["*"],        # allow all HTTP methods
    allow_headers=["*"],        # allow all headers
)

# ✅ Static files
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# ✅ Run server
if __name__ == "__main__":
    uvicorn.run("app.main:app", host=APP_HOST, port=APP_PORT, reload=True)