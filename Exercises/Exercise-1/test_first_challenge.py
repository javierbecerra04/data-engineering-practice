from main import validate_uri
from main import get_filename

def test_validate_uri():
    assert validate_uri('google.com') == False

def test_get_filename():
    assert get_filename('https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip') == 'Divvy_Trips_2020_Q1.zip'