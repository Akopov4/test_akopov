from constants import UNICORNS_ENDPOINT


class BaseRequest:
    def __init__(self,url:str=UNICORNS_ENDPOINT):
        self.base_url = url
        self.headers = {"Content-Type": "application/json; charset=utf-8"}