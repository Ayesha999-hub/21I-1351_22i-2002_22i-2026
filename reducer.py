#!/usr/bin/env python

import sys

current_word = None
word_count = 0

for line in sys.stdin:
    # Parse input from mapper
    word, count = line.strip().split("\t")
    
    # Update word count
    if current_word == word:
        word_count += int(count)
    else:
        # Emit word and total count
        if current_word:
            print(current_word, word_count)
        current_word = word
        word_count = int(count)

# Emit the last word
if current_word:
    print(current_word, word_count)
current_word = None
article_ids = set()

for line in sys.stdin:
    word, article_id = line.strip().split("\t")

    # Update set of article_ids for each word
    if current_word == word:
        article_ids.add(article_id)
    else:
        # Emit word and count of unique article_ids
        if current_word:
            print(current_word, len(article_ids))
        current_word = word
        article_ids = set([article_id])

# Emit the last word
if current_word:
    print(current_word, len(article_ids))
current_article = None
tfidf_vector = {}

for line in sys.stdin:
    article_id, word, tfidf = line.strip().split("\t")
    tfidf = float(tfidf)
    if current_article == article_id:
        tfidf_vector[word] = tfidf
    else:
        if current_article:
            # Emit article_id and TF-IDF vector
            print(current_article, tfidf_vector)
        current_article = article_id
        tfidf_vector = {word: tfidf}

# Emit the last article_id
if current_article:
    print(current_article, tfidf_vector)
#!/usr/bin/env python

import sys

for line in sys.stdin:
    print(line.strip())  # Reducer is not needed, just pass through