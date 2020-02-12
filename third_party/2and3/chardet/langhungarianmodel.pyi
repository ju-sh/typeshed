from typing import Tuple, TypedDict

class ModelType(TypedDict):
    char_to_order_map: Tuple[int]
    precedence_matrix: Tuple[int]
    typical_positive_ratio: float
    keep_english_letter: bool
    charset_name: str
    language: str

Latin2_HungarianCharToOrderMap: Tuple[int]
win1250HungarianCharToOrderMap: Tuple[int]
HungarianLangModel: Tuple[int]

Latin2HungarianModel: ModelType
Win1250HungarianModel: ModelType
