from typing import Any


class S3SignedUrl:
    def __init__(self, url: str, fields: dict[Any, str]):
        self.url = url
        self.fields = fields
