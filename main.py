from fastapi import FastAPI
from routes.user_routes import user_router
from db import get_db

app = FastAPI()

app.include_router(user_router)
#to create the database


@app.get("/")
def read_root():
    return {"Hello":"worl"}



if __name__ =="__main__" :
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000, reload=True)