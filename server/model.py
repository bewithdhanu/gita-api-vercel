from enum import Enum
from typing import List, Dict
from typing import Optional
from typing import Tuple
from typing import Union

from pydantic import BaseModel


####################################################################################################
# pydantic models
####################################################################################################
class GitaVerseSimple(BaseModel):
    chapter_no: int
    verse_no: int
    language: str
    chapter_name: str
    verse: Union[str, List[str]]
    audio_link: str

class GitaChapter(BaseModel):
    chapter_no: int
    chapter_name: str
    verses_count: int

class GitaVerse(BaseModel):
    chapter_no: int
    verse_no: Union[int, List[int]]
    language: str
    chapter_name: str
    verse: Union[str, List[str]]
    transliteration: Optional[Union[str, List[str]]] = ""
    synonyms: Optional[Union[str, List[Dict[str, str]]]] = ""
    audio_link: Optional[str] = ""
    translation: str
    purport: Union[str, List[str]]


class APIInfo(BaseModel):
    title: str
    description: str
    version: str
    supported_languages: List[str]
    total_verses: int
    documentation_url: str
    github_url: str
    features: List[str]
    endpoints: List[Dict[str, str]]


class Language(str, Enum):
    telugu = "tel"
    odia = "odi"
    english = "eng"
    spanish = "esp"


class APIError(BaseModel):
    error: str
    message: str
