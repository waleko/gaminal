from .column import Column
from .row import Row


class Grid(Column, list):
    def __init__(
        self,
        items_x: int,
        items_y: int,
        BaseClass: type,
        baseArgs: tuple = (),
        name: str = "",
        w=600,
        h=600,
        init_payload: dict = {},
    ):
        super().__init__(
            items_y,
            Row,
            (items_x, BaseClass, baseArgs, name, w, h // items_y),
            name,
            w,
            h,
            init_payload,
        )
