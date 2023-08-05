from .utils import Bilibili, Credential


class Live(Bilibili):
    def __init__(self, credential: Credential):
        super().__init__(credential=credential)
