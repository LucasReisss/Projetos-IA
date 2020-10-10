from fuzzywuzzy import fuzz
from fuzzywuzzy import process

fuzz.ratio("bolo de chocolate", "bolo chocolate")

fuzz.partial_ratio ("bolo de chocolate", "chocolate")

fuzz.ratio("bolo de chocolate", "chocolate bolo de")

fuzz.token_sort_ratio ("bolo de chocolate", "chocolate bolo de")

