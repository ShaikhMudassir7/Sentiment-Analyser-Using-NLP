# Cleaning text steps:
# 1) Create a text file and fetch text from import
# 2) Convert the letters to lowercase ('Apple' is not equal to 'apple')
# 3) Remove punctuation like .,!? etc (Hi! This is Mudassir's CodingHood')

# for text cleaning step
import string
# for emotion_counter
from collections import Counter
# for plotting gragh
import matplotlib.pyplot as plt


def cleaning():
    text = open('read.txt', encoding="utf-8").read()
    lower_cased = text.lower()
    cleaned_string = lower_cased.translate(
        str.maketrans('', '', string.punctuation))
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
    return final_words

    # the for loop make a temporary pointer ```words``` which'll itterate and store ```tokenized_text``` list
    # if ```word``` is not a stop_words then it will append it to ```final_words``` list
    # print(final_words)

# NLP Emotion Algorithm:
# 1) Check if the word in final words is also present in the emotion.txt file
    # - Open the emotion.txt file
    # - Loop through each line in the file and clear it
    # - Extract the word and emotion using split
# 2) if the word is present => add emotion to the emotion_list
# 3) finally count the emotion in the emotion list


def emotions():
    final_words = stopwords()
    emotion_list = []
    with open('emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')
            if word in final_words:
                emotion_list.append(emotion)
    return emotion_list

def emotions_count():
    emotion_list = emotions()
    emotion_count = Counter(emotion_list)
    print(emotion_count)
    return emotion_count

def plot_emotion():
    emotion_count = emotions_count()
    plt.bar(emotion_count.keys(),emotion_count.values() )
    plt.savefig('graph.png')
    plt.show()
    
plot_emotion()
