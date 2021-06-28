class URL:
    MAIN = "https://www.imdb.com/"
    NAME = MAIN + "name/"
    
    def name_id(id: int) -> str: return URL.NAME + "nm" + str(id).zfill(7) + "/"