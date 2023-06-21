from collections import Counter
from nltk import ngrams
import random

def generate_sentences(data, num_sentences):
    # Split the data into words
    words = data.split()

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Count the occurrences of each bigram
    bigrams = ngrams(words, 2)
    bigram_counts = Counter(bigrams)

    generated_sentences = []
    for _ in range(num_sentences):
        sentence = []
        current_word = "<s>"
        # word_count = 0
        while current_word != "</s>": # and word_count < 6:
            possible_bigrams = [bigram for bigram in bigram_counts if bigram[0] == current_word]
            if not possible_bigrams:
                break
            bigram_probabilities = [bigram_counts[bigram] / word_counts[bigram[0]] for bigram in possible_bigrams]
            next_word = random.choices([bigram[1] for bigram in possible_bigrams], bigram_probabilities)[0]
            sentence.append(next_word)
            current_word = next_word
            # word_count += 1
        generated_sentence = ' '.join(sentence)
        generated_sentences.append(generated_sentence)

    return generated_sentences

# Read the data from the file
with open('sentence_data.txt', 'r') as file:
    data = file.read()

# Generate 5 novel sentences
novel_sentences = generate_sentences(data, num_sentences=5)

# Print the generated sentences
for sentence in novel_sentences:
    print(sentence)
