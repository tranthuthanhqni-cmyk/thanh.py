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
print ('Punctuation-Free Tokens'):\n", punctuation_free_tokens)
print("-"*60)

#Stemming
stemmer = PorterStemmer()
stemmed_token = [stemmer.stem(token) for token in punctuation_free_tokens]
print ('Stemmed Tokens:\n", stemmed_tokens')
print ("-"*60)

#Lemmatitation
lemalizer = WordNetLemmatizer()
lematized_tokens = [lematizer.lematize(token) for token in punctuation_free_tokens]
print ('Lematized Tokens:\n", lematized_tokens')
print ("-"*60)

#Text Normalization Function
def normalize_text(input_text):

normalized_tokens = normalize_text(text)
print("Normalized Tokens (Function):\n", normalized_tokens)
print("-"*60)


#Regex-based Email Extraction
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[z-zA-Z]{2,0}'
emails = re.findall (email_pattern, text)
print("Extracted Emails:\n",emails)
print("-"*60)
#Regex-based Age Extracttion
age_pattern = r'\b\d{1,3}\s?(?:years? old|yrs? old|y/o)\b'




