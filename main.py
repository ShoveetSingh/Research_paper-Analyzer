from fastapi import FastAPI,Request,Depends
from fastapi.responses import JSONResponse,RedirectResponse
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,Session,DeclarativeBase
from passlib.context import CryptContext
from jose import jwt
from fastapi_mail import FastMail,MessageSchema
from pydantic import BaseModel

import redis.asyncio as redis

app=FastAPI()

r=redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

Database_url = ''


@app.get('/items/{item}')
async def home(item:int):
     await r.set('integer_item',item)
     it = await r.get('integer_item')
     if it:
          print(f'item is {it}')
     return f'{it}'

