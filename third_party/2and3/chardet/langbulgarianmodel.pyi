from typing import Tuple, TypedDict

class ModelType(TypedDict):
    char_to_order_map: Tuple[int]
    precedence_matrix: Tuple[int]
    typical_positive_ratio: float
    keep_english_letter: bool
    charset_name: str
    language: str

Latin5_BulgarianCharToOrderMap: Tuple[int]
win1251BulgarianCharToOrderMap: Tuple[int]
BulgarianLangModel: Tuple[int]
Latin5BulgarianModel: ModelType
Win1251BulgarianModel: ModelType
