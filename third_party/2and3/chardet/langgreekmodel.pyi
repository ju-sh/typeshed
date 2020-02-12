from typing import Tuple, TypedDict

class ModelType(TypedDict):
    char_to_order_map: Tuple[int]
    precedence_matrix: Tuple[int]
    typical_positive_ratio: float
    keep_english_letter: bool
    charset_name: str
    language: str

Latin7_char_to_order_map: Tuple[int]
win1253_char_to_order_map: Tuple[int]
GreekLangModel: Tuple[int]

Latin7GreekModel: ModelType
Win1253GreekModel: ModelType
