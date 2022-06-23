from urllib import response
from wsgiref import headers
import requests
import os
import zipfile

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]

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

def download_files(folder: str) -> None:
    for uri in download_uris:
        if validate_uri(uri):
            filename = get_filename(uri)
            response = requests.get(uri)
            open(os.path.join(folder,filename),"wb").write(response.content)

def unzip_files(dir: str, extension = ".zip") -> None:
    os.chdir(dir)
    for file in os.listdir(dir):
        if file.endswith(extension):
            filename = os.path.abspath(file)
            zipfile.ZipFile(filename).extractall(dir)
            os.remove(filename)

def main():
    current_dir = os.getcwd()
    downloads_folder = os.path.join(current_dir,r'downloads')
    if not os.path.exists(downloads_folder):
        os.mkdir(downloads_folder)
    download_files(downloads_folder)
    unzip_files(downloads_folder)

if __name__ == '__main__':
    main()
