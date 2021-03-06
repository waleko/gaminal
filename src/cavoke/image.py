from .unit import Unit


class Image(Unit):
    @property
    def _unit_type(self) -> str:
        return "image"

    def fullHash(self):
        return super().fullHash() + hash(self.image_url)

    def getDisplayDict(self) -> dict:
        d = super().getDisplayDict()
        d["image_url"] = self.image_url
        return d

    @property
    def image_url(self) -> str:
        return self.__image_url

    def setImageUrl(self, image_url: str):
        self.__image_url = image_url

    def __init__(
        self,
        image_url: str,
        name: str = "",
        w: int = -1,
        h: int = -1,
        init_payload: dict = {},
    ):
        super().__init__(name, w, h, init_payload)
        self.__image_url = image_url
