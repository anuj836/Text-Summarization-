import re
import math
from tkinter import Tk, Text, Label, Button, END

def tokenize_sentences(text):
    # Split the input text into sentences based on punctuation (.!?) followed by a space
    sentences = re.split(r'(?<=[.!?]) +', text)
    return [s.strip() for s in sentences if s]  # Return non-empty sentences

def tokenize_words(sentence):
    # Extract words from a sentence, converting to lowercase and removing punctuation
    return re.findall(r'\b\w+\b', sentence.lower())

def compute_tf(sentences):
    # Calculate Term Frequency (TF) for each sentence
    tf_scores = []
    for sentence in sentences:
        words = tokenize_words(sentence)  # Tokenize the sentence into words
        counts = {}
        length = len(words)  # Get the number of words in the sentence
        for w in words:
            counts[w] = counts.get(w, 0) + 1  # Count occurrences of each word
        # Normalize the counts to get TF values
        tf_scores.append({w: count/length for w, count in counts.items()})
    return tf_scores

def compute_idf(sentences):
    # Calculate Inverse Document Frequency (IDF) for all unique words across sentences
    N = len(sentences)  # Total number of sentences
    idf_counts = {}
    for sentence in sentences:
        words = set(tokenize_words(sentence))  # Unique words in the sentence
        for w in words:
            idf_counts[w] = idf_counts.get(w, 0) + 1  # Count how many sentences contain each word
    # Calculate IDF values
    return {w: math.log(N/(count)) for w, count in idf_counts.items()}

def score_sentences_tf_idf(tf_scores, idf_scores):
    # Score each sentence based on TF-IDF
    scores = []
    for tf in tf_scores:
        score = 0
        for w, tf_val in tf.items():
            score += tf_val * idf_scores.get(w, 0)  # Multiply TF by IDF for each word
        scores.append(score)  # Append the score for the sentence
    return scores

def summarize(text, max_sentences=3):
    # Main function to summarize the input text
    sentences = tokenize_sentences(text)  # Tokenize the input text into sentences
    if len(sentences) <= max_sentences:
        return text.strip()  # Return the original text if it's short enough

    tf_scores = compute_tf(sentences)  # Compute TF for each sentence
    idf_scores = compute_idf(sentences)  # Compute IDF for all words
    sentence_scores = score_sentences_tf_idf(tf_scores, idf_scores)  # Score sentences

    # Rank sentences based on their scores
    ranked_sentences = sorted(zip(sentences, sentence_scores), key=lambda x: x[1], reverse=True)
    # Select the top scored sentences and sort them by their original order
    selected = sorted(ranked_sentences[:max_sentences], key=lambda x: sentences.index(x[0]))

    # Join the selected sentences to form the summary
    summary = ' '.join([s[0] for s in selected])
    return summary

def on_summarize():
    # Function to handle the summarization process when the button is clicked
    txt_output.delete(1.0, END)  # Clear previous output
    text = txt_input.get("1.0", END)  # Get the input text from the text area
    summary = summarize(text, max_sentences=3)  # Generate the summary
    txt_output.insert(END, summary)  # Display the summary in the output text area

# GUI setup
root = Tk()  # Create the main window
root.title("TF-IDF Text Summarization Tool")  # Set the window title

Label(root, text="Input Text:").pack()  # Label for input text area
txt_input = Text(root, height=12, width=70)  # Text area for input
txt_input.pack()  # Add the input text area to the window

btn_summarize = Button(root, text="Summarize", command=on_summarize)  # Button to trigger summarization
btn_summarize.pack(pady=10)  # Add the button to the window

Label(root, text="Summary:").pack()  # Label for summary output area
txt_output = Text(root, height=8, width=70)  # Text area for output summary
txt_output.pack()  # Add the output text area to the window

root.mainloop()  # Start the Tkinter event loop
