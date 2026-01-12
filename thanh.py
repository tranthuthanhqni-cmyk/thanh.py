import nltk
import re
import string  
# Download required NLTK resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
# Input text
text = ("Im Thanh."
"my cat is black  ")
print('Original Text:\n', text)
print("-"*60)

#Tokenization
tokens = word_tokenize (text)
print("Tokens:\n", tokens)
print("-"*60)

#Lowercasting
lower_tokens = [token.lower() for token in tokens]
print ("Lowercased Tokens:\n", Lower_tokens)
print("-"*60)

#Sropword Removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in lower_tokens if token not in stop_words]
print ('Filtered Tokens (Stopwords Removed):\n', filtered_tokens)
print("-"*60)

#Punctuation Removal
punction_table = str.maketrans(",", "", string.punction)
punctuation_free_tokens = [token.translate(punctuation_table) for token in filtered tokens]


