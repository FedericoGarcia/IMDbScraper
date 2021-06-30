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
