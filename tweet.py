# load data using pandas
# perform data processing
# add search results to mongodb


import pandas as pd
from datetime import datetime
import os


class Tweets:
    """
    This object is used to process datafile(s) and provide a summary of the keyword that is searched
    """
    def __init__(self, filepath, sep=","):
        """
        Initializes the object by providing the filepath and delimiter
        :param filepath: directory of the datafile(s)
        :param sep: Separator to be used to format the provided datafile(s)
        """
        self.df = None
        for name in os.scandir(filepath):
            if name.is_file():
                if self.df is None:
                    self.df = pd.read_csv(name, sep=sep)
                else:
                    self.df.append(pd.read_csv(name, sep=sep))
        #self.df = pd.read_csv(filepath, sep=sep)
        self.df["date"] = self.df["created_at"].apply(lambda x: x.split(' ')[0])
        self.df["time"] = self.df["created_at"].apply(lambda x: x.split(' ')[1][0:5])
        self.row_count = self.df.shape[0]
        #self.filtered_df["date"] = pd.to_datetime(self.filtered_df["created_at"], utc=True).dt.date
        #self.filtered_df["time"] = pd.to_datetime(self.filtered_df["created_at"], utc=True).dt.time

        self.last_searched_term = None

    def search(self, term):
        """
        Function used to search for a keyword and returns a summary of the search
        :param term: Word to search for in the text
        :return: A payload that contains information gathered from the search
        """
        df = self.df[self.df["text"].str.contains(term)]
        self.last_searched_term = term
        payload = {
            "time_stamp": round(datetime.timestamp(datetime.now()), 0),
            "search_term": term,
            "tweets_by_date": df.groupby(["date"]).size().to_dict(),
            "unique_user": df["author_id"].nunique(),
            "average_likes": df["like_count"].sum()/df.shape[0],
            "locations": df.groupby(["place_id"]).size().to_dict(),
            "tweets_by_time": df.groupby(["time"]).size().to_dict(),
            "most_tweets": df.groupby(["author_id"]).size().to_dict()
        }
        return payload


# data = Tweets("data/Copy of correct_twitter_201904.tsv", sep="\t")
# data.search('music')
# print(data.tweet_by_time())
