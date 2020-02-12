from typing import Tuple, TypedDict

class ModelType(TypedDict):
    char_to_order_map: Tuple[int]
    precedence_matrix: Tuple[int]
    typical_positive_ratio: float
    keep_english_letter: bool
    charset_name: str
    language: str

TIS620CharToOrderMap: Tuple[int]
ThaiLangModel: Tuple[int]
TIS620ThaiModel: ModelType
