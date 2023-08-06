from .utils import requests_json, CookieTypes


async def get_qrcode(cookie: CookieTypes = None) -> dict:
    """
    获取登录二维码
    Returns:
    Args:
        cookie:

    """
    return await requests_json(url="https://passport.bilibili.com/x/passport-login/web/qrcode/generate", cookies=cookie)


async def poll_qrcode(qrcode_key: str, cookie: CookieTypes = None) -> dict:
    """
    获取二维码的状态
    Args:
        cookie:
        qrcode_key:

    Returns:

    """
    return await requests_json(
        url=f"https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key={qrcode_key}", cookies=cookie)
