# %% import
import sys  # isort:skip
sys.path.append(
    '/Users/papanash/workspace/datastory-org/data-science/projects/newspackage')

import datetime as dt
# %% Imports and settings
import os
import warnings

import matplotlib.pyplot as plt
# (df_corpus
#     .groupby('source')
#     .size()
#     .sort_values()
#     .plot('barh', title='Number of articles per organization', alpha=0.5));
# %% Newspaper3k
import newspaper
import numpy as np
import pandas as pd
from newspaper import Article

from src.corpus import CorpusLoader
from src.download import NewsFetcher

plt.style.use('seaborn-whitegrid')
pd.options.mode.chained_assignment = None
# %matplotlib inline
# % configInlineBackend.figure_format = 'retina'


# %%
# Instantiate NewsFetcher with default domains
fetcher = NewsFetcher()


# %%
# Search a given time period

r = fetcher.fetch_period(datetime.datetime(
    2020, 9, 16, 7), end=datetime.datetime(2020, 9, 16, 12))


df_20_9_16 = pd.DataFrame(r)


# %% save
df_20_9_16.to_csv('./data/raw/2020-09-16.csv', index=False, compression='gzip')

# %%
cols = [
    'Aftonbladet',
    'Dagens Nyheter',
    'Expressen',
    'GöteborgsPosten',
    'Svenska Dagbladet',
    'Sveriges Radio - Ekot',
    'Sveriges Television',
    'Sydsvenskan']

# %% Load data and  Publication frequency

# corpus_loader = CorpusLoader(use_cache=False)
# df = corpus_loader.load_docs()
# df = df[df['source'].isin(cols)]
# df['indexed'] = pd.to_datetime(df['indexed'])

url = 'https://www.theguardian.com/us-news/2020/sep/20/supreme-court-joe-biden-donald-trump-republicans-mcconnell-abuse-of-power-ruth-bader-ginsburg'
urlDN = 'https://www.dn.se/ekonomi/sankta-skatter-och-valfardsmiljarder-i-budgeten/'

article = Article(urlDN)
article.download()
article.html
article.parse()
article.authors


article.publish_date
article.text
article.top_image
article.nlp()
article.keywords
article.summary


cnn_paper = newspaper.build('http://cnn.com')
# for article in cnn_paper.articles:
#     print(article.url)
for category in cnn_paper.category_urls():
    print(category)
