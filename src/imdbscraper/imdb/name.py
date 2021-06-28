import datetime

import bs4
import pandas
import requests

class Biography:
    def extract(url: str):
        page = requests.get(url + "bio")
        page_raw = page.text
        page_html_parsed = bs4.BeautifulSoup(page_raw, "lxml")
        
        try:
            overview_table = pandas.read_html(page_raw, attrs = {"id": "overviewTable"})[0]
            overview_table.columns = ["field", "value"]
            overview_table = overview_table.set_index("field")
        except:
            overview_table = None

        try:
            spouses_table = pandas.read_html(page_raw, attrs = {"id": "tableSpouses"})
        except:
            spouses_table = None  

        try:
            salaries_table = pandas.read_html(page_raw, attrs = {"id": "salariesTable"})
        except:
            salaries_table = None

        try:
            name = page_html_parsed.find("div", {"class": "subpage_title_block"}).find("div", {"class": "parent"}).find("h3").find("a").text
        except:
            name = None
        
        try:
            born = overview_table.loc["Born", "value"].rsplit(" in\xA0")
        except:
            born = None

        try: # full date
            birthday = datetime.datetime.strptime(born[0], "%B %d, %Y")
            birthday = birthday.strftime("%Y-%m-%d")
        except:
            try: # year only
                birthday = datetime.datetime.strptime(born[0], "%Y")
                birthday = birthday.strftime("%Y")
            except:
                birthday = None

        try:
            birthplace = born[1]
        except:
            birthplace = None

        try:
            birth_name = overview_table.loc["Birth Name", "value"]
        except:
            birth_name = None

        try:
            height = overview_table.loc["Height", "value"]
            height = height.rsplit("\xA0(")[1]
            height = height.rsplit("\xA0")[0]
            height = float(height)
        except:
            height = None

        return {
            "name": name,
            "birthday": birthday,
            "birthplace": birthplace,
            "birth_name": birth_name,
            "height": height
        }
