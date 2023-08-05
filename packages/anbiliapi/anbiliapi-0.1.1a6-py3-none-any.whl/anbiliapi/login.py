from .utils import requests_json


async def get_qrcode() -> dict:
    """
    获取登录二维码
    Returns:

    """
    return await requests_json(url="https://passport.bilibili.com/x/passport-login/web/qrcode/generate")


async def poll_qrcode(qrcode_key: str) -> dict:
    """
    获取二维码的状态
    Args:
        qrcode_key:

    Returns:

    """
    return await requests_json(
        url=f"https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key={qrcode_key}")
