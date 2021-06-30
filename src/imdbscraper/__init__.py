import datetime

import bs4
import pandas
import requests

import imdbscraper.imdb
import imdbscraper.imdb.name

__version__ = '0.1.1'

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
    def birth_day(self) -> str: return self.__biography["birth_day"]

    @property
    def birth_place(self) -> str: return self.__biography["birth_place"]

    @property
    def birth_name(self) -> str: return self.__biography["birth_name"]

    @property
    def death_day(self) -> str: return self.__biography["death_day"]

    @property
    def death_place(self) -> str: return self.__biography["death_place"]

    @property
    def death_cause(self) -> str: return self.__biography["death_cause"]

    @property
    def height(self) -> float: return self.__biography["height"]