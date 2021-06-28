import datetime

import bs4
import pandas
import requests

import imdbscraper.imdb
import imdbscraper.imdb.name

__version__ = '0.1.0'

class Name:
    def __init__(self, id: int) -> None:
        self.__id = id
        self.__url = imdbscraper.imdb.URL.name_id(self.id)
        self.__biography = imdbscraper.imdb.name.Biography.extract(self.__url)
        
    @property
    def id(self) -> int:
        if self.__id > 0:
            return self.__id
        else:
            raise ValueError("id must be greater than 0")

    @property
    def url(self) -> str: return self.__url

    @property
    def name(self) -> str: return self.__biography["name"]

    @property
    def birthday(self) -> str: return self.__biography["birthday"]

    @property
    def birthplace(self) -> str: return self.__biography["birthplace"]

    @property
    def birth_name(self) -> str: return self.__biography["birth_name"]

    @property
    def height(self) -> float: return self.__biography["height"]