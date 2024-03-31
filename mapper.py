#!/usr/bin/env python

import sys
import re
from collections import Counter
import math

# Regular expression to match words
WORD_RE = re.compile(r"\b\w+\b")

for line in sys.stdin:
    # Tokenize the input text into words
    words = re.findall(WORD_RE, line.lower())
    for word in words:
        # Emit word count of 1 for each word
        print(word, 1)
# Regular expression to match words
WORD_RE = re.compile(r"\b\w+\b")

for line in sys.stdin:
    article_id, text = line.strip().split(",", 1)
    words = set(re.findall(WORD_RE, text.lower()))
    for word in words:
        # Emit word and article_id
        print(word, article_id)


# Regular expression to match words
WORD_RE = re.compile(r"\b\w+\b")

def calculate_tf(word_counts):
    total_words = sum(word_counts.values())
    tf = {word: count / total_words for word, count in word_counts.items()}
    return tf

def calculate_idf(article_count, word_count):
    return math.log(article_count / (1 + word_count))

for line in sys.stdin:
    article_id, text = line.strip().split(",", 1)
    words = re.findall(WORD_RE, text.lower())
    word_counts = dict(Counter(words))
    tf = calculate_tf(word_counts)
    for word, count in tf.items():
        # Emit article_id and TF-IDF weight for each word
        print(article_id, word, count * calculate_idf(TOTAL_ARTICLES, len(word_counts)))
# Regular expression to match words
WORD_RE = re.compile(r"\b\w+\b")

# Load query text from command line argument
query = sys.argv[1]

# Tokenize and preprocess the query text
query_words = set(re.findall(WORD_RE, query.lower()))

for line in sys.stdin:
    article_id, tfidf_vector = line.strip().split("\t", 1)
    tfidf_vector = eval(tfidf_vector)  # Convert string representation to dictionary
    relevance_score = 0
    
    # Calculate relevance score between query and document TF-IDF vectors
    for word in query_words:
        if word in tfidf_vector:
            relevance_score += query_words[word] * tfidf_vector[word]  # TF-IDF weights multiplication
    
    # Emit article_id and relevance score
    print(article_id, relevance_score)