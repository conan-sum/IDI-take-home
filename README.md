## Getting Started

1. Clone this repository
2. Create a directory named `data` and place all the datafiles with the same format inside
3. Create a virtual environment to run the code
```commandline
python -m venv tweets
source venv/bin/activate
pip install -r requirements.txt
python run.py
```
This will let you install all required packages and run the Flask server without using your actual Python installation

## Documentation

### Tweets
This is the object that does all the filtering and querying based on the entered search term, it is broken down into two separate parts:
#### 1. Reading data file(s)
In order for the API to function properly, all datafile(s) with the same format must be placed within the `data` directory. 
#### 2. Searching and generating summary
After you enter a search term into the API call, the code will go through all the data that was loaded into the first part and look for all the tweets that contain the search term. Then it will generate a summary of the results and output it as a JSON object

## API Endpoints
After you have successfully started the API, there are two endpoints that can be used

#### 1.`home`
This is the default endpoint to notify the user that they have established a connection to the API, nothing needs to be done at this point
#### 2. `search/<term>`
This is the endpoint where the user can use to search for keywords in the datafile(s) loaded in at the first step

#### Example
You can use the API by entering this URL into Chrome
```commandline
http://127.0.0.1:5000/search/music
```
This URL searches for the keyword `music` within the datafiles, and it will generate a summary of the results
```commandline
{
    "time_stamp": 1719512836,
    "search_term": "music",
    "tweets_by_date": Object,
    "unique_user": 1563,
    "average_likes": 234.05348380765457,
    "locations": Object,
    "tweets_by_time": Object,
    "most_tweets": Object
}
```
The result will then be stored into MongoDB for future references