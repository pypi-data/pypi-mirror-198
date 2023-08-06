from http.cookiejar import CookieJar
from typing import Dict, List, Tuple, Union

CookieTypes = Union["Cookies", CookieJar, Dict[str, str], List[Tuple[str, str]]]
