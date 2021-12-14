import aiohttp
import asyncio

DEBUG = True
BASE_URL = 'http://127.0.0.1:8000' if DEBUG else ''


async def get_categories():
    async with aiohttp.ClientSession() as session:
        async with session.get('/api/shop/category-list/') as response:
            response = await response.json()
            print(response)


async def get_shops_by_category(category_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'/api/shop/shop-get-by-category/{category_id}') as response:
            response = await response.json()
            print(response)


async def get_shops():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'/api/shop/shop-list/') as response:
            response = await response.json()
            print(response)


async def search_product_in_shop(shop_id: int, product_name: str):
    return {}


async def create_shop(username: str, description: str, category_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'/api/shop/shop-list/') as response:
            response = await response.json()
            print(response)


async def update_shop(shop_id: int, description: str, category_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'/api/shop/shop-list/') as response:
            response = await response.json()
            print(response)


async def remove_shop(shop_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.delete(f'/api/shop/shop-delete/{shop_id}') as response:
            response = await response.json()
            print(response)


async def create_product(shop_id: int, description: str, photo: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'/api/shop/shop-list/') as response:
            response = await response.json()
            print(response)


async def update_product(product_id: int, description: str, photo: str):
    async with aiohttp.ClientSession() as session:
        async with session.put(f'/api/shop/shop-list/') as response:
            response = await response.json()
            print(response)


async def remove_product(product_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.delete(f'/api/shop/card-delete/{product_id}') as response:
            response = await response.json()
            print(response)


async def get_shops_by_username(username: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'/api/shop/shop-get-by-username/{username}') as response:
            response = await response.json()
            print(response)
