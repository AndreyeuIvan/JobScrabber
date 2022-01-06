from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import dev_parser, hh_parser
from db import engine
from models import Base


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(hh_parser.router)
app.include_router(dev_parser.router)

@app.get('/')
def main():
    return RedirectResponse('/docs')

