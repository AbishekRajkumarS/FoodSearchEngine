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

df = pd.read_csv('IndianFood.csv', nrows=1000)
display(df)

df['PreProcessing'] = df['TranslatedRecipeName'].map(str) + ' ' + df['TranslatedIngredients'].map(str) + ' ' + df['Cuisine'].map(str) + df['Course'].map(str) + ' ' + df['Diet'].map(str) + df['TranslatedInstructions'].map(str)

count = 0
for data in df['PreProcessing']:
    data = data.lower() # Converts to lower case   
    data = re.sub(r'\d+', '', data) # Removes numbers
    data = re.sub(" +|\n|\r|\t|\0|\x0b|\xa0", ' ', data).strip()   
    data = data.translate(data.maketrans(string.punctuation,' '*len(string.punctuation))) # Removes punctuation
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(data)
    result = [i for i in tokens if not i in stop_words] # Stopword removal
    lemmatizer=WordNetLemmatizer()
    final = ''
    for word in result:
        final = final + ' ' + lemmatizer.lemmatize(word) + ' '
    df['PreProcessing'][count] = final
    count = count+1
display(df)

data = df.reset_index()

index = {}
for indexNo, m in data.iterrows():
    words = m.PreProcessing.split()
    ID = indexNo
    for word in words:
        if word in index.keys():
            if ID not in index[word]:
                index[word].append(ID)
        else:
            index[word] = [ID]
print(index)