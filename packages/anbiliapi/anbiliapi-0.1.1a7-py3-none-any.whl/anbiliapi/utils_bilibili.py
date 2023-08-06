from .utils import requests, CookieTypes


async def get_buvid3() -> str:
    return (await requests(url="https://www.bilibili.com/")).cookies.get("buvid3")


async def get_init_cookie() -> CookieTypes:
    return (await requests(url="https://www.bilibili.com/")).cookies
