import imdbscraper


actor = {
    "astaire": imdbscraper.Name(1),
    "niro": imdbscraper.Name(134),
    "depp": imdbscraper.Name(136),
    "dicaprio": imdbscraper.Name(138),
    "streep": imdbscraper.Name(658),
    "swank": imdbscraper.Name(5476),
    "adolph": imdbscraper.Name(12345)
}

def test_id():
    assert actor["astaire"].id == 1
    assert actor["niro"].id == 134
    assert actor["depp"].id == 136
    assert actor["dicaprio"].id == 138
    assert actor["streep"].id == 658
    assert actor["swank"].id == 5476
    assert actor["adolph"].id == 12345

def test_url():
    assert actor["astaire"].url == "https://www.imdb.com/name/nm0000001/"
    assert actor["niro"].url == "https://www.imdb.com/name/nm0000134/"
    assert actor["depp"].url == "https://www.imdb.com/name/nm0000136/"
    assert actor["dicaprio"].url == "https://www.imdb.com/name/nm0000138/"
    assert actor["streep"].url == "https://www.imdb.com/name/nm0000658/"
    assert actor["swank"].url == "https://www.imdb.com/name/nm0005476/"
    assert actor["adolph"].url == "https://www.imdb.com/name/nm0012345/"

def test_name():
    assert actor["astaire"].name == "Fred Astaire"
    assert actor["niro"].name == "Robert De Niro"
    assert actor["depp"].name == "Johnny Depp"
    assert actor["dicaprio"].name == "Leonardo DiCaprio"
    assert actor["streep"].name == "Meryl Streep"
    assert actor["swank"].name == "Hilary Swank"
    assert actor["adolph"].name == "Jörg Adolph"

def test_birth_day():
    assert actor["astaire"].birth_day == "1899-05-10"
    assert actor["niro"].birth_day == "1943-08-17"
    assert actor["depp"].birth_day == "1963-06-09"
    assert actor["dicaprio"].birth_day == "1974-11-11"
    assert actor["streep"].birth_day == "1949-06-22"
    assert actor["swank"].birth_day == "1974-07-30"
    assert actor["adolph"].birth_day == "1967"

def test_birth_place():
    assert actor["astaire"].birth_place == "Omaha, Nebraska, USA"
    assert actor["niro"].birth_place == "New York City, New York, USA"
    assert actor["depp"].birth_place == "Owensboro, Kentucky, USA"
    assert actor["dicaprio"].birth_place == "Hollywood, Los Angeles, California, USA"
    assert actor["streep"].birth_place == "Summit, New Jersey, USA"
    assert actor["swank"].birth_place == "Lincoln, Nebraska, USA"
    assert actor["adolph"].birth_place == "Herford, Germany"

def test_birth_name():
    assert actor["astaire"].birth_name == "Frederic Austerlitz Jr."
    assert actor["niro"].birth_name == "Robert Anthony De Niro Jr."
    assert actor["depp"].birth_name == "John Christopher Depp II"
    assert actor["dicaprio"].birth_name == "Leonardo Wilhelm DiCaprio"
    assert actor["streep"].birth_name == "Mary Louise Streep"
    assert actor["swank"].birth_name == "Hilary Ann Swank"
    assert actor["adolph"].birth_name == None

def test_death_day():
    assert actor["astaire"].death_day == "1987-06-22"
    assert actor["niro"].death_day == None
    assert actor["depp"].death_day == None
    assert actor["dicaprio"].death_day == None
    assert actor["streep"].death_day == None
    assert actor["swank"].death_day == None
    assert actor["adolph"].death_day == None

def test_death_place():
    assert actor["astaire"].death_place == "Los Angeles, California, USA"
    assert actor["niro"].death_place == None
    assert actor["depp"].death_place == None
    assert actor["dicaprio"].death_place == None
    assert actor["streep"].death_place == None
    assert actor["swank"].death_place == None
    assert actor["adolph"].death_place == None

def test_death_cause():
    assert actor["astaire"].death_cause == "pneumonia"
    assert actor["niro"].death_cause == None
    assert actor["depp"].death_cause == None
    assert actor["dicaprio"].death_cause == None
    assert actor["streep"].death_cause == None
    assert actor["swank"].death_cause == None
    assert actor["adolph"].death_cause == None

def test_height():
    assert actor["astaire"].height == 1.75
    assert actor["niro"].height == 1.77
    assert actor["depp"].height == 1.73
    assert actor["dicaprio"].height == 1.83
    assert actor["streep"].height == 1.68
    assert actor["swank"].height == 1.68
    assert actor["adolph"].height == None