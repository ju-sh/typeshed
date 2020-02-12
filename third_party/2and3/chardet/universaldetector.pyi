from typing import Dict, Union, AnyStr, Pattern, TypedDict
from logging import Logger

class ResultType(TypedDict):
    encoding: str
    confidence: float
    language: str

class UniversalDetector(object):
    MINIMUM_THRESHOLD: float
    HIGH_BYTE_DETECTOR: Pattern[bytes]
    ESC_DETECTOR: Pattern[bytes]
    WIN_BYTE_DETECTOR: Pattern[bytes]
    ISO_WIN_MAP: Dict[str, str]

    result: ResultType
    done: bool
    lang_filter: int
    logger: Logger

    def __init__(self, lang_filter: int) -> None: ...
    def reset(self) -> None: ...
    def feed(self, byte_str: bytes) -> None: ...
    def close(self) -> ResultType: ...
