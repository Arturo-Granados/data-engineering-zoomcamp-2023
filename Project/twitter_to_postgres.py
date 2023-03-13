import tweepy
import configparser
import pandas as pd
from pathlib import Path
from prefect import flow, task




def get_authentication_keys(path: Path) -> str:

  config = configparser.ConfigParser()
  config.read(path)

  consumer_key = config['twitter']['consumer_key']
  consumer_secret = config['twitter']['consumer_secret']

  access_token = config['twitter']['access_token']
  access_token_secret = config['twitter']['access_token_secret']

  return consumer_key, consumer_secret, access_token, access_token_secret


def authenticacion(consumer_key, consumer_secret, access_token, access_token_secret) -> None:

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)


  return tweepy.API(auth, wait_on_rate_limit=True)


def verification(api):

  try:
    api.verify_credentials()
    print('Successful Authentication')
  except:
    print('Failed authentication')


def get_hasstags(woeid: int, api) -> list:

  trending_topics = api.trends_place(woeid)

  hashtags = []

  for trend in trending_topics[0]["trends"]:
    hashtags.append(trend["name"])

  return hashtags


def tweets_to_df(api, hashtags: list) -> pd.DataFrame:
  
  columns = ['Time','hashtag', 'Tweet']
  data=[]
  for hashtag in hashtags:
    hashtag_tweets = tweepy.Cursor(api.search, q=hashtag).items(1)
    for tweet in hashtag_tweets:
      data.append([tweet.created_at,hashtag, tweet.text])

  df = pd.DataFrame(data, columns=columns)
  return df 


## Cleaning data ## 

#Lowercasing all the letters
def tweet_lowercasing(df: pd.DataFrame) -> pd.DataFrame:
  df['Tweet'] = df['Tweet'].apply(lambda x: x.lower())
  return df

#Removing hashtags and mentions
def removing_hashtags(df: pd.DataFrame) -> pd.DataFrame:
  df['Tweet'] = df['Tweet'].apply(lambda x: re.sub("@[A-Za-z0-9_]+","", x))
  df['Tweet'] = df['Tweet'].apply(lambda x: re.sub("#[A-Za-z0-9_]+","", x))
  return df

# Removing links
def removing_links(df: pd.DataFrame) -> pd.DataFrame:
  df['Tweet'] = df['Tweet'].apply(lambda x: re.sub(r"http\S+", "", x))
  df['Tweet'] = df['Tweet'].apply(lambda x: re.sub(r"www.\S+", "", x))
  return df

# Removing punctuations
def removing_punctuations(df: pd.DataFrame) -> pd.DataFrame:
  df['Tweet'] = df['Tweet'].apply(lambda x: re.sub('[()!?]', ' ', x))
  df['Tweet'] = df['Tweet'].apply(lambda x: re.sub('\[.*?\]',' ', x))
  return df

# Removing non-alphanumeric characters
def removing_nonalphanumeric(df: pd.DataFrame) -> pd.DataFrame:
  df['Tweet'] = df['Tweet'].apply(lambda x: re.sub("[^a-z0-9]"," ", x))
  return df

# Remove rt flag
def remove_rt_flag(df: pd.DataFrame) -> pd.DataFrame:
  rt_flag = 'rt'
  df['Tweet'] = df['Tweet'].apply(lambda x: x.replace(rt_flag, ""))
  return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
  df = tweet_lowercasing(df)
  df = removing_hashtags(df)
  df = removing_links(df)
  df = removing_punctuations(df)
  df = removing_nonalphanumeric(df)
  df = remove_rt_flag(df)
  return df


#Funcion para guardar los datos es la maquina local(task)
def write_in_local(df: pd.DataFrame, path: Path) -> None:
  df.to_csv(path)

#Funcion para extraer tweets y guardarlos en local(flow)
def twitter_to_local() -> None:
    config_path = Path("C:/Users/art_g/OneDrive/Escritorio/de-zoomcamp/data-engineering-zoomcamp-2023/Project/config.ini")
    store_csv_path = Path('C:/Users/art_g/OneDrive/Escritorio/de-zoomcamp/data-engineering-zoomcamp-2023/Project/data/data.csv')
    woeid = 116545
    api_key, api_key_secret, access_token, access_token_secret = get_authentication_keys(config_path)
    api = authenticacion(api_key, api_key_secret, access_token, access_token_secret)
    verification(api)
    hashtags = get_hasstags(woeid, api)
    data = tweets_to_df(api, hashtags)
    data = write_in_local(data, store_csv_path)
    

if __name__ == '__main__':
    
    twitter_to_local()
        


