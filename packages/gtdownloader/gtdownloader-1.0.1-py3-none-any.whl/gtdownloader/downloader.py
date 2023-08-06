"""
COMPLEX AND SUSTAINABLE URBAN NETWORKS LAB
Leveraging
@author: Juan Acosta
"""
import os
import time
import pandas as pd

from ._utils.utils import *

import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
# from searchtweets import collect_results, load_credentials
from .geomethods import TweetGeoGenerator
from .apicall import retrieve_tweets

from wordcloud import WordCloud, STOPWORDS


class TweetDownloader:
    """Tweet downloading class.
    The TweetDownloader class contains the main downloading function
    as well as the storing and plotting functions accessible to the
    user.

    Parameters
    ----------
    credentials : str
        A path pointing to the location of the TwitterAPI credentials file.
    name : str, optional
        The name to use when saving downloaded files and exports.
        The default value 'Project_[date]' with the current date in
        %m%d%Y_%H%M%S format.
    output_folder : str, optional
        Path to the folder in which saved information is going to be stored.
        It defaults to the current location


    Attributes
    ----------
    credentials : str
        A path pointing to the location of the TwitterAPI credentials file.
    name : str, optional
        The name to use when saving downloaded files and exports.
    output_folder : str, optional
        Path to the folder in which saved information is going to be stored.
    tweets : list
        List of pages of the response tweet object obtained from Twitter
        API calls.
    authors : list
        List of pages of the response authors object obtained from Twitter
        API calls.
    places : list
        List of pages of the response location object obtained from Twitter
        API calls.
    replies : list
        List of tweets that are replies to the tweets in the tweets attribute
    tweets_df : pandas.DataFrame
        Table with the tweets from the attribute tweets
    authors_df : pandas.DataFrame
        Table with the authors from the attribute authors
    places_df : pandas.DataFrame
        Table with the georreferenced locations from the attribute places
    replies_df : pandas.DataFrame
        Table containing replies to the tweets in the tweets_df table
    search_args : dict
        Dictionary containing the Twitter keys required to access the API
    timestamp : str
        A string to append at the end of saved files, so they all have a
        timestamp
    """

    def __init__(self,
                 yaml_credentials=None,
                 env_token=None,
                 bearer_token=None,
                 name=None,
                 output_folder=''):
        if name == None:
            self.name = 'Project_{}'.format(datetime.now().strftime('%m%d%Y_%H%M%S'))
        else:
            self.name = name
        self.credentials = yaml_credentials
        self.output_folder = output_folder
        self.tweets = None
        self.authors = None
        self.places = None
        self.replies = None
        self.tweets_df = None
        self.authors_df = None
        self.places_df = None
        self.replies_df = None
        self.timestamp = None
        self.env_token = env_token
        self.bearer_token = bearer_token

    def tweets_from_query(self, query_params, max_page, save_temp, max_tweets, reply_mode=False):
        # initializes a list to store retrieved tweet pages
        list_tweet_pages = []
        # initializes tweet page count
        page_count = 1
        # initializes retrieved tweets count
        tweet_count = 0
        # count to stop algorithm when search has no results
        zeros_count = 0

        filename = self.name

        # Creates data frames to store tweets, locations, and author data
        df_tweets = pd.DataFrame()
        df_places = pd.DataFrame()
        df_authors = pd.DataFrame()
        # loop that ends whenever desired number of tweets is retrieved
        while True:

            # Collect results according to query parameters, tweets per page...
            # ... and authentication credentials

            # tweets_page = collect_results(query_params, max_tweets=max_page,
            #                              result_stream_args=self.search_args)

            if self.credentials != None:
                keys = self.credentials
            elif self.env_token != None:
                keys = self.env_token
            elif self.bearer_token != None:
                keys = self.bearer_token
            else:
                raise AttributeError('No authentication keys provided')

            tweets_page = retrieve_tweets(query_params=query_params, keys=keys)

            if len(tweets_page) != 0:  # ensures we don't process a blank page

                # Adds retrieved page of tweets to list of pages
                list_tweet_pages.append(tweets_page)

                # Adds number of retrieved tweets to tweet count
                tweet_count += tweets_page['meta']['result_count']
                try:
                    df_page = pd.DataFrame(tweets_page['data'])
                except KeyError:
                    continue
                df_page_authors = pd.DataFrame(tweets_page['includes']['users'])

                df_tweets = pd.concat([df_tweets, df_page])
                df_authors = pd.concat([df_authors, df_page_authors])

                try:
                    df_page_places = pd.DataFrame(tweets_page['includes']['places'])
                    df_places = pd.concat([df_places, df_page_places])
                except KeyError:
                    # print('No places on this page...')
                    # print('Building DataFrame from Tweet pages...')
                    pass

                # resets index of dataframes to avoid redundancy after concatenation
                df_tweets.reset_index(drop=True, inplace=True)
                df_places.reset_index(drop=True, inplace=True)
                df_authors.reset_index(drop=True, inplace=True)

                # saving temporal dataframes
                if save_temp & (not reply_mode):
                    df_tweets.to_csv(os.path.join(self.output_folder, f'temp_{filename}_tweets_{self.timestamp}'),
                                     index=False)
                    df_places.to_csv(os.path.join(self.output_folder, f'temp_{filename}_places_{self.timestamp}'),
                                     index=False)
                    df_authors.to_csv(
                        os.path.join(self.output_folder, f'temp_{filename}_authors_{self.timestamp}'),
                        index=False)

                    print('Current progress saved at:',
                          os.path.join(self.output_folder, f'temp_{filename}_{self.timestamp}'))

                if save_temp & reply_mode:
                    df_tweets.to_csv(os.path.join(self.output_folder, f'temp_{filename}_replies_{self.timestamp}'),
                                     index=False)
                    print('Current progress saved at:',
                          os.path.join(self.output_folder, f'temp_{filename}_{self.timestamp}'))

                # Checks whether there are more pages and goes onto the next page...
                try:
                    if (not reply_mode):
                        print('Ending page %s with next_token=%s. %s tweets retrieved (%s total)' % (
                            page_count, tweets_page['meta']['next_token'], tweets_page['meta']['result_count'],
                            tweet_count))
                    next_token = tweets_page['meta']['next_token']
                    query_params['next_token'] = next_token
                    page_count += 1
                    time.sleep(5)

                # ...or if final page is reached then the loop ends
                except KeyError:
                    # print('Ending page %s. This was the final page. %s tweets retrieved' % (page_count, tweet_count))
                    break
                # Ends loop if maximum number of tweets is reached
                if (tweet_count >= max_tweets) & (not reply_mode):
                    print('Intended amount of tweets reached. %s tweets retrieved. Goal was %s' % (
                        tweet_count, max_tweets))
                    break
            else:
                # print('This tweets page had 0 tweets')
                zeros_count += 1
                if zeros_count > 1:
                    break

        return list_tweet_pages, df_tweets, df_places, df_authors

    def get_tweets(self, query,
                   start_time=None,
                   end_time=None,
                   lang=None, include_retweets=False, place=None, has_geo=True,
                   max_tweets=10, max_page=500, save_temp=True, save_final=True,
                   save_replies=False, include_replies=False, max_replies=10, temp_replies=True):
        """
        Parameters
        ----------
        query : str
            Words to be searched in tweets. Twitter API query operators supported.
        start_time : str
            Lower bound of  time frame in which tweets are going to be searched in date-time format (default is current date and time minus 24 hours)
        end_time : str
            Upper bound of time frame in which tweets are going to be searched in date-time format (default is current date and time time)
        lang : str, optional
            Two letter code for language to be imposed in retrieved tweets
        include_retweets : bool
            Whether to include tweets that are just a retweet of a previous one (default is False)
        place : str, optional
            Two letter code for country or place in which the search is going to be constraint
        has_geo : bool, optional
            Whether to only include tweets with geographic reference (default is True)
        max_tweets : int
            The maximum amount of tweets to retrieve in total (default is 10)
        max_page : int
            The maximum amount of tweets allowed per tweets page (default is 500)
        save_temp : bool
            Whether to save current progress (default is True)
        save_final : bool
            Whether to save final tweets dataframe after download is over (default is True)
        save_replies : bool
            Whether to include the replies to the downoaded tweets (default is false)
        max_replies : bool
            Maximum amount of replies per tweet if replies are allowed (default is 10)
        temp_replies : bool
            Whether to save progress while downloading replies if these are allowed (default is True)
        """

        if start_time == None:
            start_time = validate_date((datetime.now() - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%Sz"))
        if end_time == None:
            end_time = validate_date((datetime.now() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%Sz"))

        # Query parameters
        query = '({})'.format(query)
        # Creates a timestamp to avoid overwriting old files
        self.timestamp = datetime.now().strftime('%m%d%Y_%H%M%S.csv')

        if lang:
            query += f' (lang:{lang})'
        if place:
            query += f' (place_country:{place})'
        if has_geo:
            query += ' (has:geo)'
        if not include_retweets:
            query += ' (-is:retweet)'

        max_page = max_tweets if max_tweets <= max_page else max_page

        query_params = {'query': query,
                        'start_time': validate_date(start_time),
                        'end_time': validate_date(end_time),
                        'expansions': 'geo.place_id,author_id',
                        'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
                        'tweet.fields': 'created_at,author_id,id,public_metrics,conversation_id',
                        'user.fields': 'id,location,name,username,public_metrics',
                        'max_results': max_page
                        }

        print('Downloading tweets...')

        self.tweets, self.tweets_df, self.places_df, self.authors_df = self.tweets_from_query(query_params, max_page,
                                                                                              save_temp, max_tweets)

        filename = os.path.join(self.output_folder, self.name)

        print(f'Tweets download done. A total of {self.tweets_df.shape[0]} tweets were retrieved.')

        try:
            self.tweets_df['place_id'] = self.tweets_df.geo.apply(lambda x: get_attribute_from_dict(x, 'place_id'))
        except AttributeError:
            self.tweets_df['place_id'] = np.nan
        # Creates date column in date format
        self.tweets_df['date'] = pd.to_datetime(self.tweets_df.created_at)
        self.tweets_df['date'] = self.tweets_df.date.dt.strftime('%m/%d/%Y %H:%M:%S')
        self.tweets_df['date'] = pd.to_datetime(self.tweets_df['date'], utc=False, format='%m/%d/%Y %H:%M:%S')

        # Get metrics as separate columns:
        self.tweets_df['likes'] = self.tweets_df.public_metrics.apply(lambda x: x['like_count'])
        self.tweets_df['replies'] = self.tweets_df.public_metrics.apply(lambda x: x['reply_count'])
        self.tweets_df['retweets'] = self.tweets_df.public_metrics.apply(lambda x: x['retweet_count'])

        if save_final:
            # saving final dataframes

            self.tweets_df.to_csv(f'{filename}_tweets_{self.timestamp}', index=False)
            self.places_df.to_csv(f'{filename}_places_{self.timestamp}', index=False)
            self.authors_df.to_csv(f'{filename}_authors_{self.timestamp}', index=False)

            print('csv files {}, {}, and {} were generated'.format(f'{filename}_tweets_{self.timestamp}',
                                                                   f'{filename}_places_{self.timestamp}',
                                                                   f'{filename}_authors_{self.timestamp}'))

        if include_replies:
            print('Preparing to get tweet replies...')
            if len(self.tweets) > 0:
                self.replies_df = self.get_replies(max_replies=max_replies,
                                                   save_temp=temp_replies, save_final=save_replies)
            else:
                print('There were no tweets to get replies from')

        # Still unsure about whether to have values to unpack or just have the attributes updated
        #    return self.tweets_df, self.places_df, self.authors_df, self.replies_df

        # else:
        #    return self.tweets_df, self.places_df, self.authors_df,

    def get_replies(self, max_replies=10, save_temp=True, save_final=True):
        """
        Parameters
        ----------
        max_replies : int
            Maximum number of replies for each tweet in the original tweets dataset (default is 10)
        save_temp : bool
            Whether to save progress at each page (default is True)
        save_final : bool,
            Whether to save final replies dataset (default is True)
        """

        df_tweets_rep = pd.DataFrame()

        print('Downloading replies... this might take some time')

        total_tweets = self.tweets_df.query('replies>0').shape[0]
        rep_count = 0
        total_replies = 0

        filename = os.path.join(self.output_folder, self.name)

        for conversation_id in self.tweets_df.query('replies>0').conversation_id:
            rep_count += 1

            print(f'getting replies for tweet {rep_count} out of {total_tweets} (total replies so far:{total_replies})')

            query = f'conversation_id:{conversation_id}'

            # Maximum amount of tweets to retrieve. This is only the maximum and not a
            # Maximum tweets retrieved on each "page". Must be integer between 10 and 500
            max_tweets_page = max_replies if max_replies <= 500 else 500

            # query parameters. For info see:
            # https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all

            query_params = {'query': query,
                            'start_time': '2007-01-01T00:00:00z',
                            'end_time': validate_date(
                                (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%Sz")),
                            'expansions': 'author_id',
                            'tweet.fields': 'created_at,author_id,id,conversation_id',
                            'user.fields': 'id,name,username,public_metrics',
                            'max_results': max_tweets_page
                            }

            time.sleep(5)
            self.replies, df_replies, _, _ = self.tweets_from_query(query_params, max_tweets_page,
                                                                    save_temp, max_replies, reply_mode=True)
            df_tweets_rep = pd.concat([df_tweets_rep, df_replies])

            total_replies = df_tweets_rep.shape[0]

            if total_replies >= max_replies:
                print('The desired maximum amount of replies was reached.')
                break

        if save_final:
            df_tweets_rep.to_csv(f'{filename}_replies_{self.timestamp}', index=False)

        self.replies_df = df_tweets_rep

        print(f'Replies download done. {total_replies} reply tweets were downloaded')

        return df_tweets_rep

#    def build_dataframes(self):
#        # Loop that goes through the tweet pages and stores data in DataFrames
#        print('Building DataFrame from Tweet pages...')
#
#        df_tweets = pd.DataFrame()
#        df_places = pd.DataFrame()
#        df_authors = pd.DataFrame()
#
#        for page in self.tweets:
#            df_page = pd.DataFrame(page[0]['data'])
#            df_page_authors = pd.DataFrame(page[0]['includes']['users'])
#
#            try:
#                df_page_places = pd.DataFrame(page[0]['includes']['places'])
#                df_places = pd.concat([df_places, df_page_places])
#            except KeyError:
#                print('No places on this page...')
#                print('Building DataFrame from Tweet pages...')
#            df_tweets = pd.concat([df_tweets, df_page])
#            df_authors = pd.concat([df_authors, df_page_authors])
#
#        # resets index of dataframes to avoid redundancy after concatenation
#        df_tweets.reset_index(drop=True, inplace=True)
#        df_places.reset_index(drop=True, inplace=True)
#        df_authors.reset_index(drop=True, inplace=True)
#
#        self.tweets_df = df_tweets
#        self.places_df = df_places
#        self.authors_df = df_authors
#
#        print('Done')

    def tweets_from_csv(self, path, sep=',', save_temp=True):
        """
        Parameters
        ----------
        path : str
            The path to the csv path containing the download parameters
        sep : str, optional
            The separator of the csv file (default is ,)
        save_temp : bool, optional
            Whether to save or not progress at each downloaded page (default is True)
        """

        # loading config values into a DataFrame
        df_param = pd.read_csv(path, sep=sep)

        # storing parameters into variables to be passed to the query obj
        query = df_param.query('parameter=="query"')['value'].item()
        start_time = validate_date(df_param.query('parameter=="start_time"')['value'].item())
        end_time = validate_date(df_param.query('parameter=="end_time"')['value'].item())
        max_tweets_total = int(df_param.query('parameter=="max_tweets"')['value'].item())
        max_tweets_page = int(df_param.query('parameter=="max_tweets_page"')['value'].item())
        filename = df_param.query('parameter=="filename"')['value'].item()
        plot_wordcloud = df_param.query('parameter=="wordcloud"')['value'].item()
        plot_barplot = df_param.query('parameter=="barplot"')['value'].item()
        custom_stopwords = df_param.query('parameter=="stopwords"')['value'].item()
        lang = df_param.query('parameter=="language"')['value'].item()
        place = df_param.query('parameter=="place"')['value'].item()
        include_retweets = df_param.query('parameter=="include_retweets"')['value'].item()
        has_geo = df_param.query('parameter=="only_georreferenced"')['value'].item()

        self.name = filename

        if pd.isna(start_time): start_time = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%Sz")
        if pd.isna(end_time): end_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        if pd.isna(place): place = None
        if pd.isna(lang): lang = None

        if not pd.isna(lang):
            query += f' (lang:{lang})'
        if not pd.isna(place):
            query += f' (place_country:{place})'
        if has_geo == 'yes':
            query += ' (has:geo)'
        if include_retweets != 'yes':
            query += ' (-is:retweet)'

        # Query parameters. See the parameters.csv to modify or see the description
        # of each parameter
        query_params = {'query': query,
                        'start_time': start_time,
                        'end_time': end_time,
                        'expansions': 'geo.place_id,author_id',
                        'place.fields': 'contained_within,country,country_code,full_name,geo,id,name,place_type',
                        'tweet.fields': 'created_at,author_id,id,public_metrics,conversation_id',
                        'user.fields': 'id,location,name,username,public_metrics',
                        'max_results': max_tweets_page
                        }
        # Creates a timestamp to avoid overwriting old files
        self.timestamp = datetime.now().strftime('_%m%d%Y_%H%M%S.csv')

        # Gets tweets
        self.tweets, self.tweets_df, self.places_df, self.authors_df = self.tweets_from_query(query_params,
                                                                                              max_tweets_page,
                                                                                              save_temp,
                                                                                              max_tweets_total,
                                                                                              reply_mode=False)

        if plot_wordcloud.lower() == 'yes':
            words_tuple = ast.literal_eval(custom_stopwords)
            stopwords_list = [i.strip() for i in words_tuple]
            if plot_barplot.lower() == 'yes':
                plot_barplot = True
            else:
                plot_barplot = False
            self.wordcloud(custom_stopwords=stopwords_list, save_wordcloud=True,
                           bar_plot=plot_barplot, save_bar_plot=True)

    def tweets_to_gdf(self, geo_type='centroids'):
        """
        Parameters
        ----------
        geo_type : {'centroids', 'bbox'}, optional
            The type of geometry (default is centroids)
        """
        tgeo = TweetGeoGenerator(self)
        tgeo.create_gdf()
        gdf_tweets = tgeo.get_tweets_gdf(geo_type)
        return gdf_tweets

    def places_to_gdf(self, geo_type='centroids'):
        """
        Parameters
        ----------
        geo_type : {'centroids', 'bbox'}, optional
            The type of geometry (default is centroids)
        """
        tgeo = TweetGeoGenerator(self)
        tgeo.create_gdf()
        gdf_places = tgeo.get_places_gdf(geo_type)
        return gdf_places

    def preview_tweet_locations(self):
        tgeo = TweetGeoGenerator(self)
        tgeo.create_gdf()
        tgeo.simple_tweets_map()

    def interactive_map(self):
        print('Generating map...')
        tgeo = TweetGeoGenerator(self)
        tgeo.create_gdf()
        tgeo.plot_tweets_points()
        print('Done. Map will be displayed in browser')

    def interactive_map_agg(self):
        print('Generating map...')
        tgeo = TweetGeoGenerator(self)
        tgeo.create_gdf()
        tgeo.plot_tweets_aggregated()
        print('Done. Map will be displayed in browser')

    def plot_heatmap(self, radius=20):
        """
        Parameters
        ----------
        radius : int
            The radius of the heatmap plot (default is 20)
        """
        tgeo = TweetGeoGenerator(self)
        tgeo.create_gdf()
        tgeo.plot_tweets_heatmap(radius)

    def map_animation(self, time_unit):
        """
        Parameters
        ----------
        time_unit : {'second', 'minute', 'hour', 'day', 'month', 'year'}
            Time unit to aggregate by (default is 'day')
        """
        print('Generating map animation...')
        tgeo = TweetGeoGenerator(self)
        tgeo.create_gdf()
        tgeo.bubble_animation(time_unit)
        print('Done. Animation will be displayed in browser')

    def wordcloud(self, custom_stopwords=None, background_color='black', min_word_length=4,
                  save_wordcloud=True, bar_plot=False, save_bar_plot=False):

        """
        Parameters
        ----------
        custom_stopwords : list
            List of words to exclude from word cloud
        background_color : {'black', 'white'}
            Background color of wordcloud plot
        min_word_length : int
            Minimum length of strings to be considered for word cloud (default is 4)
        save_wordcloud: bool,
            Whether to save plot (default is True)
        bar_plot: bool
            Whether to display barplot with word frequency (default is False)
        save_bar_plot:
            Whether to save barplot (default is False)
        """

        if custom_stopwords is None:
            custom_stopwords = []
        plt.rcParams.update({'font.size': 12})

        # custom_stopwords.append('http')
        # custom_stopwords.append('https')

        df_tweets = self.tweets_df.copy()

        # gets all text contained in tweets
        text = " ".join(review for review in df_tweets.text.astype(str))
        print("There are {} words in the combination of all cells in column text.".format(len(text)))

        # stopwords are the words we don't want to take into account in wordclouds or wordcounts
        stopwords = set(STOPWORDS)
        # update this list with your desired stopwords
        stopwords.update(custom_stopwords)

        # creates wordcloud using the wordcloud library, stopwords, and tweets text
        wordcloud = WordCloud(stopwords=stopwords, background_color=background_color,
                              collocations=False, min_word_length=min_word_length,
                              width=600, height=300).generate(text)

        # plots wordcloud
        plt.figure(figsize=(15, 7))
        plt.tight_layout(pad=0)
        plt.imshow(wordcloud, interpolation='bilinear')
        ax = plt.gca()
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        if save_wordcloud:
            plt.savefig(os.path.join(self.output_folder, f'{self.name}_wordcloud.png'))
            print('Wordcloud saved at', os.path.join(self.output_folder, f'{self.name}_wordcloud.png'))
        else:
            plt.show(block=False)

        if bar_plot:
            # creates a dataframe to handle wordcount retrieved from wordcloud
            df_wordcount = pd.DataFrame(wordcloud.process_text(text).items(),
                                        columns=['word', 'freq'])
            # sorts word count in descending order
            df_wordcount.sort_values('freq', ascending=False, inplace=True)

            # plots word count bar chart
            plt.figure(figsize=(40, 20))
            plt.xticks(fontsize=40)
            plt.yticks(fontsize=40)
            plt.xlabel("freq", fontsize=50)
            plt.ylabel("word", fontsize=50)
            plt.savefig(os.path.join(self.output_folder, f'{self.name}_wordcloud.png'))

            df_bar_plot = df_wordcount[:20].copy()

            if save_bar_plot:
                sns.barplot(data=df_bar_plot,
                            x='word',
                            y='freq').get_figure().savefig(os.path.join(self.output_folder,
                                                                                      f'{self.name}_barplot.png'))
                print('Barplot saved at', os.path.join(self.output_folder, f'{self.name}_barplot.png'))
            else:
                sns.barplot(data=df_bar_plot,
                            x='word',
                            y='freq').get_figure()
                plt.show(block=False)
