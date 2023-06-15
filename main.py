# Cleaning text steps:
# 1) Create a text file and fetch text from import
# 2) Convert the letters to lowercase ('Apple' is not equal to 'apple')
# 3) Remove punctuation like .,!? etc (Hi! This is Mudassir's CodingHood')
import string


def cleaning():
    text = open('read.txt',encoding="utf-8").read()
    lower_cased = text.lower()
    cleaned_string = lower_cased.translate(str.maketrans('','',string.punctuation))
    # the str.maketrans have three parameter x,y and z
    # x is the text to be replaced
    # y is the text by which x will be replaced
    # z is the text to be deleted
    return cleaned_string

# Tokenization & stop words steps:
# 1) Tokenization is to break the input strings into list (for e.g: ['I','Love','Python'])
# 2) Sentence should be breaked into words because NLP is Processing of Words
# 3) Stop words are the words which doesn't add any meaning to the sentence i.e 'I' doesn't add any emotion

def tokenization():
    cleaned_string = cleaning()
    tokenized_text = cleaned_string.split()
    return tokenized_text
def stopwords():
    # stop word list 
    tokenized_text = tokenization()
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    final_words = []
    for words in tokenized_text:
        if words not in stop_words:
            final_words.append(words)
    # the for loop make a temporary pointer ```words``` which'll itterate and store ```tokenized_text``` list
    # if ```word``` is not a stop_words then it will append it to ```final_words``` list
    # print(final_words)
stopwords()

