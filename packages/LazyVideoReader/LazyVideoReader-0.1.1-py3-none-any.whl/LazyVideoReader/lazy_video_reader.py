from itertools import islice
from typing import Generator, Iterable

import numpy as np
from cv2 import VideoCapture


def create_video_reader(path: str) -> Generator[np.ndarray, None, None]:
    cap = VideoCapture(path)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret is False:
            cap.release()
            return
        yield frame


def take(end: int, iterator: Iterable) -> Iterable:
    return islice(iterator, 0, end)


def drop(start: int, iterator: Iterable) -> Iterable:
    return islice(iterator, start)


def head(iterator: Iterable) -> Iterable:
    return next(iterator)


def tail(iterator: Iterable) -> Iterable:
    return drop(1, iterator)
