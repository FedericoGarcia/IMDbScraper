import datetime
import re

import bs4
import pandas
import requests


class Biography:

    def get_overview_table(page_raw: str):
        try:
            overview_table = pandas.read_html(page_raw, attrs = {"id": "overviewTable"})[0]
            overview_table.columns = ["field", "value"]
            overview_table = overview_table.set_index("field")
        except:
            overview_table = None
        return overview_table
    
    def get_spouses_table(page_raw: str):
        try:
            spouses_table = pandas.read_html(page_raw, attrs = {"id": "tableSpouses"})
        except:
            spouses_table = None
        return spouses_table

    def get_salaries_table(page_raw: str):
        try:
            salaries_table = pandas.read_html(page_raw, attrs = {"id": "salariesTable"})
        except:
            salaries_table = None
        return salaries_table
    
    def get_name(page_raw: str, page_parsed: bs4.BeautifulSoup) -> str:
        try:
            name = page_parsed.find("div", {"class": "subpage_title_block"}).find("div", {"class": "parent"}).find("h3").find("a").text
        except:
            name = None
        return name
    
    def get_born(overview_table: pandas.DataFrame) -> str:
        try:
            born = re.split(" in\xA0", overview_table.loc["Born", "value"])
        except:
            born = None
        return born
    
    def get_birth_day(born: str) -> str:
        try: # full date
            birth_day = datetime.datetime.strptime(born[0], "%B %d, %Y")
            birth_day = birth_day.strftime("%Y-%m-%d")
        except:
            try: # year only
                birth_day = datetime.datetime.strptime(born[0], "%Y")
                birth_day = birth_day.strftime("%Y")
            except:
                birth_day = None
        return birth_day
    
    def get_birth_place(born: str) -> str:
        try:
            birth_place = born[1]
        except:
            birth_place = None
        return birth_place
    
    def get_birth_name(overview_table: pandas.DataFrame) -> str:
        try:
            birth_name = overview_table.loc["Birth Name", "value"]
        except:
            birth_name = None
        return birth_name
    
    def get_died(overview_table: pandas.DataFrame) -> str:
        try:
            died = re.split(" in\xA0" + "|" + " [(]" + "|" + "[)]", overview_table.loc["Died", "value"])
        except:
            died = None
        return died

    def get_death_day(died: str) -> str:
        try: # full date
            death_day = datetime.datetime.strptime(died[0], "%B %d, %Y")
            death_day = death_day.strftime("%Y-%m-%d")
        except:
            try: # year only
                death_day = datetime.datetime.strptime(died[0], "%Y")
                death_day = death_day.strftime("%Y")
            except:
                death_day = None
        return death_day

    def get_death_place(died: str) -> str:
        try:
            death_place = died[1]
        except:
            death_place = None
        return death_place

    def get_death_cause(died: str) -> str:
        try:
            death_cause = died[2]
        except:
            death_cause = None
        return death_cause

    def get_height(overview_table: pandas.DataFrame) -> float:
        try:
            height = overview_table.loc["Height", "value"]
            height = re.split("\xA0[(]" + "|" + "\xA0m[)]", height)[1] # Gets what lies between "&nbsp;(" and "&nbsp;m)"
            height = height.replace(",", ".")
            height = float(height)
        except:
            height = None
        return height

    def extract(url: str) -> dict:
        page = requests.get(url + "bio")
        page_raw = page.text
        page_parsed = bs4.BeautifulSoup(page_raw, "lxml")
        
        overview_table = Biography.get_overview_table(page_raw)
        born = Biography.get_born(overview_table)
        died = Biography.get_died(overview_table)

        spouses_table = Biography.get_spouses_table(page_raw)
        salaries_table = Biography.get_salaries_table(page_raw)
        
        return {
            "name": Biography.get_name(page_raw, page_parsed),
            "birth_day": Biography.get_birth_day(born),
            "birth_place": Biography.get_birth_place(born),
            "birth_name": Biography.get_birth_name(overview_table),
            "death_day": Biography.get_death_day(died),
            "death_place": Biography.get_death_place(died),
            "death_cause": Biography.get_death_cause(died),
            "height": Biography.get_height(overview_table)
        }
