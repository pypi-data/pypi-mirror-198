from typing import List, Set

from .corpus_types import Word
from .stopwords import STOPWORDS
from .wordnet import WORDNET


def get_stopwords() -> Set[Word]:
    """get the set data type stopwords."""
    stopwords = STOPWORDS.get("stopwords", [])
    stopwords = set(stopwords)
    return stopwords


def get_synonyms(word: Word) -> List[Word]:
    """get synonyms of the word from WordNet."""
    synonyms = WORDNET.get(word, [])
    return synonyms
