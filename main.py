from fastapi import FastAPI
import redis.asyncio as redis

app=FastAPI()

r=redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)


@app.get('/items/{item}')
async def home(item:int):
     await r.set('integer_item',item)
     it = await r.get('integer_item')
     if it:
          print(f'item is {it}')
     return f'{it}'

