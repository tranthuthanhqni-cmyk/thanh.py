import nltk
import stanza
import re
import string  
# Download required NLTK resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
stanza.download('en')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

#Initialize Stanza pipeline
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

#Input text for analysis
text = ("My name is Thanh. I'm 19 years old. I live in Hanoi. "
"I love programming in Python! "
"Natural Language Processing is fascinating.")
#Print original text
print("Original Text:\n",text)
print("-"*60)
#NLTK Sentence Segmentation
nltk_sentences = sent_tokenize(text) #Split text into sentences
print("NLTK Sentence Segmentation:")
for i, sentence in enumerate(nltk_sentences,1): #Enumerate sentences with numbering
    print(f"Sentence {i}: {sentence}")
    print("-"*60)
#NLTK Word Tokenization
nltk_words = word_tokenize(text) #Split text into words/tokens
print("NLTK Word Tokenization:")
print (nltk_words)
print("-"*60)
#NLTK Normalization
#Lowercasing all words
lowercased_words = [word.lower() for word in nltk_words] #Convert all tokens  to lowercase
print("Lowercased Words:")
print(lowercased_words)
print("."*60)
#Removing punctuation
punctuation_removed_words= [word for word in lowercased_words if word not in string.punctuation]  #Remove punctuation from tokens
print("PUNCTUATION REMOVED WORDS.")                              
print(punctuation_removed_words)
print("-"*60)
#Reconstruct normalized text
normalized_textn=' '.join(punctuation_removed_words) #Join tokens back into a single string
print("Normalized Text:\n", normalized_textn)
print("-"*60)
#Stanza POS Tagging
doc = nlp(normalized_textn) #Run Stanza pipeline on normalized text
print("Stanza POS Tagging:")
for sentence in doc.sentences: #Iterate through sentences
    for word in sentence.words: #Iterate through words 
       print(f"Word: {word.text}\tPOS: {word.upos}") #Print word + POS tag
print("-"*60)
