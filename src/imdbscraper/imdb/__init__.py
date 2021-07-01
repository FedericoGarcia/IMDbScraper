'''
                                 IMDbScraper
                   A web scraper to extract data from IMDb

Copyright (C) 2021  Federico García <garciafedericoagustin@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

class URL:
    MAIN = "https://www.imdb.com/"
    NAME = MAIN + "name/"
    
    def name_id(id: int) -> str: return URL.NAME + "nm" + str(id).zfill(7) + "/"