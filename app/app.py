import uvicorn
from models.database import engine
from models import models
from fastapi import FastAPI
from api import router
from settings import settings
models.Base.metadata.create_all(engine)
app = FastAPI(version='0.1',
              title='Приложение FastAPI',
              description='Реализованы CRUD операции'
              )

app.include_router(router)



if __name__ == "__main__":
    uvicorn.run(
        'app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
