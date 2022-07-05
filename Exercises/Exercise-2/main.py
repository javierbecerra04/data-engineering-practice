from operator import concat
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

URL = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"

def url_by_date(usr_date: str) -> str:
    if usr_date:
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, 'lxml')
        for tr in soup.body.table.find_all('tr')[3:-1]:
            date = tr.find_all('td')[1].contents[0]
            date = date.rstrip()
            if (date == usr_date):
                file_name = tr.find_all('td')[0].contents[0].contents[0]
                return URL + file_name
    return 'Didnt find a file with the given date'

def validate_uri(uri: str) -> bool:
    try:    
        headers = requests.head(uri).headers
        if headers['Content-Length']:
            return True
        return False
    except:
        return False

def get_filename(uri: str) -> str:
    if uri.find('/'):
        return uri.rsplit('/',1)[-1]

def download_file(folder: str, uri: str) -> None:
    if validate_uri(uri):
        filename = get_filename(uri)
        response = requests.get(uri)
        open(os.path.join(folder,filename),"wb").write(response.content)

def main():
    usr_date = '2022-02-07 14:03'
    url_download = url_by_date(usr_date)
    download_file(os.getcwd(),url_download)
    file_name = get_filename(url_download)
    df = pd.read_csv(file_name)
    print(df.sort_values(by=['HourlyDryBulbTemperature'],ascending=False).reset_index().iloc[0])

if __name__ == '__main__':
    main()
