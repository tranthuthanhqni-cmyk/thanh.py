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
print
