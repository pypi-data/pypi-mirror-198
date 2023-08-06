from typing import TypeAlias

from typing_extensions import Self

class Annotation:
    id: int
    image_id: int
    category_id: int
    segmentation: Polygon | PolygonRS | Rle | EncodedRle
    area: float
    bbox: Bbox
    iscrowd: int

class Category:
    id: int
    name: str
    supercategory: str

    def __init__(self: Self, id: int, name: str, supercategory: str) -> None: ...

class Bbox:
    left: float
    top: float
    width: float
    height: float

    def __init__(self: Self, left: float, top: float, width: float, height: float) -> None: ...

class Image:
    id: int
    width: int
    height: int
    file_name: str

Polygon: TypeAlias = list[list[float]]

class PolygonRS:
    size: list[int]
    counts: list[list[float]]

class Rle:
    size: list[int]
    counts: list[int]

class EncodedRle:
    size: list[int]
    counts: str
