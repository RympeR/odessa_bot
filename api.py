import aiohttp
import asyncio


async def get_categories():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/shop/get-categories/') as response:
            response = await response.json()
            print(response)


async def create_category(category_name: str):
    return {}


async def get_shops_by_category(category_id: int):
    return {}


async def get_shops():
    return {}


async def get_categories_by_shop(shop_id: int):
    return {}


async def search_product_in_shop(shop_id: int, product_name: str):
    return {}


async def create_shop(username: str, description: str, category_id: int):
    return {}


async def update_shop(shop_id: int, description: str, category_id: int):
    return {}


async def remove_shop(shop_id: int):
    return {}


async def create_product(shop_id: int, description: str, photo: str):
    return {}


async def update_product(product_id: int, description: str, photo: str):
    return {}


async def remove_product(product_id: int):
    return {}


async def get_shops_by_username(username: str):
    return {}
