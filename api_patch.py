import random
import types

categories = [
    {
        'pk': 1,
        'category_name': 'test',
    },
    {
        'pk': 2,
        'category_name': 'test',
    },
]

shops = [
    {
        'pk': 1,
        'user': 'use-test',
        'name': 'test-shop',
        'description': 'big such big',
        'categories': [
            1, 2
        ]
    },
    {
        'pk': 1,
        'user': 'use-test',
        'name': 'test-shop',
        'description': 'big such big',
        'categories': [
            1, 2
        ]
    },
    {
        'pk': 2,
        'user': 'use-test-2',
        'name': 'test-shop-2',
        'description': 'big such big 2',
        'categories': [
            1
        ]
    },
]

products = [
    {
        'pk': 1,
        'shop': {
                'pk': 1,
                'user': 'use-test',
                'name': 'test-shop',
                'description': 'big such big',
                'categories': [
                    1, 2
                ]
            },
        'attachments': [
            {
                'pk': 1,
                'file_': 'https://content2.rozetka.com.ua/goods/images/big/218590474.jpg'
            },
            {
                'pk': 2,
                'file_': 'https://content2.rozetka.com.ua/goods/images/big/218590474.jpg'
            },
        ],
        'description': 'tweewewffefwewef',
        'price': 123
    }
]

async def get_categories():
    global categories
    return {
        'results': categories
    }


async def create_category(category_name: str):
    global categories
    categories.append(
        {
            'pk': random.randint(1, 9999),
            'category_name': category_name,
        }
    )
    return True


async def get_shops_by_category(category_id: int):
    return shops


async def get_shops_by_username(username: str):
    return shops


async def get_shops():
    return shops


async def get_categories_by_shop(shop_id: int):
    return categories


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


async def update_product(product_id: int, description: str, attachments: list):
    return {}


async def remove_product(product_id: int):
    return {}
