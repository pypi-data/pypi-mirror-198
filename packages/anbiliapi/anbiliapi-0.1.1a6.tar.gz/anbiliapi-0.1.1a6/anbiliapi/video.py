from .utils import Bilibili, Credential, requests
from .utils.err import ArgsException


async def get_video_info(aid: int = None, bvid: str = None) -> dict:
    """获取视频信息

    Args:
        aid (int, optional): _description_. Defaults to None.
        bvid (str, optional): _description_. Defaults to None.

    Returns:
        dict: _description_
    """
    if aid is None and bvid is None:
        assert ArgsException("aid,bvid不能同时为None")

    kwargs = {
        "url": "https://api.bilibili.com/x/web-interface/view",
        "method": "GET",
        "params": {"aid": aid} if bvid is None else {"bvid": bvid}
    }
    res = await requests(**kwargs)
    return res.json()


class Video(Bilibili):
    def __init__(self, credential: Credential, aid: int = None, bvid: str = None, proxies=None) -> None:
        super().__init__(credential, proxies)
        if aid is None and bvid is None:
            assert ArgsException("aid,bvid不能同时为None")

        self._aid = aid
        self._bid = bvid
        self._id = {"aid": aid} if bvid is None else {"bvid": bvid}

    async def get_video_info(self) -> dict:
        """
        获取视频信息
        :return:
        """
        kwargs = {
            "url": "https://api.bilibili.com/x/web-interface/view",
            "method": "GET",
            "params": self._id
        }
        res = await self._requests_json(**kwargs)
        return res

    async def like(self, like: bool = True) -> dict:
        """
        点赞
        :param like:
        :return:
        """
        data = {"like": 1 if like else 2, "csrf": self._csrf}
        data.update(self._id)
        kwargs = {
            "url": "https://api.bilibili.com/x/web-interface/archive/like",
            "method": "POST",
            "data": data
        }
        res = await self._requests_json(**kwargs)
        return res

    async def coin(self, multiply: int = 1, select_like: bool = True) -> dict:
        """
        投币
        :param select_like:
        :param multiply:
        :return:
        """
        data = {"multiply": 2 if multiply != 1 else 1, "csrf": self._csrf, "select_like": 1 if select_like else 0}
        data.update(self._id)
        kwargs = {
            "url": "https://api.bilibili.com/x/web-interface/coin/add",
            "method": "POST",
            "data": data
        }
        res = await self._requests_json(**kwargs)
        return res

    async def add_toview(self, aid: int = None) -> dict:
        """添加到稍后观看

        Args:
            aid (int, optional): 视频av号. Defaults to None.

        Returns:
            _type_: _description_
        """
        data = {"aid": aid, "csrf": self._csrf}
        kwargs = {
            "url": "https://api.bilibili.com/x/v2/history/toview/add",
            "method": "POST",
            "data": data
        }
        res = await self._requests_json(**kwargs)
        return res

    async def del_toview(self, aid: int = None) -> dict:
        """移出稍后观看

        Args:
            aid (int, optional): 视频av号. Defaults to None.

        Returns:
            _type_: _description_
        """
        data = {"aid": aid, "csrf": self._csrf}
        kwargs = {
            "url": "https://api.bilibili.com/x/v2/history/toview/del",
            "method": "POST",
            "data": data
        }
        res = await self._requests_json(**kwargs)
        return res
