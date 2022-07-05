from main import url_by_date

def test_url_by_date():
    assert url_by_date('2022-02-07 14:03') == 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/01011099999.csv'
    assert url_by_date('1999-01-24 18:00') == 'Didnt find a file with the given date'