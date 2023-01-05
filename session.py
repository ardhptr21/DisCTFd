from requests import Response, Session
from config import HOST, TOKEN
from urllib.parse import urljoin 

class CTFdSession(Session):
    def __init__(self):
        super().__init__()
        self.headers.update({
            "Authorization": f"token {TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        })
        self.endpoint = urljoin(HOST, "/api/v1/")

    def get(self, url: str, **kwargs) -> Response:
        if url[0] == "/":
            url = url[1:]
        url = urljoin(self.endpoint, url)
        return super().get(url, **kwargs)

session = CTFdSession()