from tweet import Tweets
import numpy as np
from database import cols
import json
import pytest


def test_initialization():
    data = Tweets("data", sep="\t")
    assert data.df is not None
    assert data.row_count > 0


def test_search_keys():
    data = Tweets("data", sep="\t")
    payload = data.search("music")
    assert payload is not None
    assert len(payload) == 8
    assert type(payload) is dict


def test_search_values():
    data = Tweets("data", sep="\t")
    payload = data.search("music")
    assert payload["search_term"] == "music"

    assert type(payload["time_stamp"]) is float
    assert type(payload["search_term"]) is str
    assert type(payload["tweets_by_date"]) is dict
    assert type(payload["unique_user"]) is int
    assert type(payload["average_likes"]) is np.float64
    assert type(payload["locations"]) is dict
    assert type(payload["tweets_by_time"]) is dict
    assert type(payload["most_tweets"]) is dict


def test_database():
    data = Tweets("data", sep="\t")
    payload = data.search("music")
    cols.insert_one(json.loads(json.dumps(payload)))
    result = cols.find_one({"search_term": "music"})
    assert result is not None
    assert result["time_stamp"] == payload["time_stamp"]
