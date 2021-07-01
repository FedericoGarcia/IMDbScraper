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

import imdbscraper.imdb.name
import pandas


def test_get_height():
    overview_table = pandas.DataFrame(
        [
            ["Height", "5'\xA07¾\x22\xA0(1,72\xA0m)"]
        ]
    )
    overview_table.columns = ["field", "value"]
    overview_table = overview_table.set_index("field")

    assert imdbscraper.imdb.name.Biography.get_height(overview_table) == 1.72
