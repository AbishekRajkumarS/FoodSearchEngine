import pandas as pd
from IPython.display import display
import re
import nltk
nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
nltk.download('stopwords')
# nltk.download('punkt')
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# from nltk.corpus import wordnet
# from nltk import pos_tag
# from nltk.stem import WordNetLemmatizer 
import string

df = pd.read_csv('IndianFood.csv', nrows=10)
display(df)

indexDict = {}

for data in df['PreProcessing']:
    words = data.split(' ')
    