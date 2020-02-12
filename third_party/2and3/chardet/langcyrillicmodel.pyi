from typing import Tuple, TypedDict

class ModelType(TypedDict):
    char_to_order_map: Tuple[int]
    precedence_matrix: Tuple[int]
    typical_positive_ratio: float
    keep_english_letter: bool
    charset_name: str
    language: str

KOI8R_char_to_order_map: Tuple[int]
win1251_char_to_order_map: Tuple[int]
latin5_char_to_order_map: Tuple[int]
macCyrillic_char_to_order_map: Tuple[int]
IBM855_char_to_order_map: Tuple[int]
IBM866_char_to_order_map: Tuple[int]
RussianLangModel: Tuple[int]

Koi8rModel: ModelType
Win1251CyrillicModel: ModelType
Latin5CyrillicModel: ModelType
MacCyrillicModel: ModelType
Ibm866Model: ModelType
Ibm855Model: ModelType
