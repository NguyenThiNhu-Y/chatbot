# import nltk
# from nltk.corpus import wordnet

# def synonym_replacement(sentence):
#     words = nltk.word_tokenize(sentence)
#     new_sentence = sentence
#     for word in words:
#         synonyms = []
#         for syn in wordnet.synsets(word):
#             for lemma in syn.lemmas():
#                 synonyms.append(lemma.name())
#         if synonyms:
#             new_sentence = new_sentence.replace(word, synonyms[0])
#     return new_sentence

# # Example Usage
# original_sentence = "bạn tên gì"
# rewritten_sentence = synonym_replacement(original_sentence)
# print("Original Sentence: ", original_sentence)
# print("Rewritten Sentence: ", rewritten_sentence)

import nltk
from nltk.corpus import wordnet

# Tạo đối tượng WordNet
synonyms = []
antonyms = []

word = input("Nhập câu cần tìm đồng nghĩa: ")

for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())

# In kết quả
print("Các đồng nghĩa của từ", word, "là:")
print(set(synonyms))

if len(antonyms) > 0:
    print("Các từ trái nghĩa của từ", word, "là:")
    print(set(antonyms))
