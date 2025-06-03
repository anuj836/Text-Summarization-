#  Text-Summarization

*COMPANY* : CODETECH IT SOLUTIONS

*NAME* : ANUJ DESHMUKH

*INTERN ID* : CT04DL900

*DURATION* : 4 weeks

*MENTOR* : NEELA SANTOSH

# Description


This Python script is a TF-IDF-based text summarization tool that uses a graphical user interface (GUI) built with Tkinter. It enables users to input a block of text, process it through natural language processing (NLP) techniques, and produce a concise summary by selecting the most informative sentences. The summarization is performed using Term Frequency-Inverse Document Frequency (TF-IDF), a statistical method used to evaluate the importance of a word in a document relative to a corpus.

The script starts by importing essential modules: re for regular expressions, math for logarithmic calculations, and tkinter for the GUI. The tool is composed of several functions, each with a distinct role in processing and summarizing the text.

The first function, tokenize_sentences(text) , splits the input text into individual sentences. It uses regular expressions to detect punctuation marks (periods, exclamation marks, or question marks) followed by spaces, which typically denote sentence boundaries. This function returns a list of non-empty, stripped sentences.

The second function, tokenize_words(sentence), breaks down a single sentence into lowercase words, removing punctuation. It uses a regular expression that captures word boundaries and returns a clean list of word tokens.

Next, the function compute_tf(sentences) calculates the term frequency (TF) for each word within a sentence. It counts the number of times a word appears in the sentence and normalizes this count by the total number of words in that sentence. The output is a list of dictionaries, each corresponding to a sentence and mapping words to their respective TF values.

The function compute_idf(sentences) computes the inverse document frequency (IDF) of each word across all sentences. It iterates through all sentences, counts how many contain each unique word, and applies the IDF formula:

$$
IDF(w) = \log\left(\frac{N}{\text{count}(w)}\right)
$$

where N is the total number of sentences, count(w) is the number of sentences containing the word $w$. This step helps in reducing the weight of commonly occurring words that are less informative.

The function score_sentences_tf_idf(tf_scores, idf_scores) computes the TF-IDF score for each sentence. It multiplies each word’s TF value by its IDF score, summing them to produce a total score for each sentence. These scores indicate the relevance of the sentences in the overall text.

The core summarization function, summarize(text, max_sentences=3), orchestrates the process. It first tokenizes the text into sentences and checks if the total number is less than or equal to the desired summary length. If so, it returns the original text. Otherwise, it calculates TF and IDF values, scores each sentence, and selects the top-scoring ones. These top sentences are then ordered according to their original appearance in the text to maintain coherence.

The GUI portion uses Tkinter to create an interactive interface. A Text  widget is used for input, where the user can enter or paste text. A "Summarize" button calls the on_summarize() function, which retrieves the input text, generates a summary, and displays it in a second Text widget labeled as "Summary."

The GUI is simple and intuitive, providing an effective way to demonstrate extractive summarization based on TF-IDF. It is especially useful in educational settings or for quick summarization tasks. While not as advanced as abstractive models using transformers or deep learning, this approach remains fast, interpretable, and easy to implement.

Overall, this script combines classical NLP techniques with a user-friendly interface, making it a practical tool for understanding the mechanics of text summarization.
