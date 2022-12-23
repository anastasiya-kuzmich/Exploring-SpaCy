# Exploring-SpaCy

This is an exploratory repository in which I tested out the capabilities of [spaCy](spacy.io): an open-source software library for advanced natural language processing. I learned how to use the package, correctly reference into its structures, employ various pre-processing methods, improve runtime and performance and apply its built-in and custom pipelines.

I used data from the [Toxic Comment Classification Challenge](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/overview) to build a text classifcation model capable of detecting different types of of toxicity (e.g. threats, obscenity, insults, and identity-based hate) in comments from Wikipedia’s talk page edits. My best model achieved the following AUC scores in predicting the toxicity labels:

    toxic 0.963
    severe_toxic 0.987
    obscene 0.987
    threat 0.973
    insult 0.976
    identity_hate 0.959
    non_toxic 0.965

I additionally followed the [Text classification with an RNN](https://www.tensorflow.org/text/tutorials/text_classification_rnn) tutorial to run a basic classification task using TensorFlow. My best model achieved 0.95 in accuracy at predicting whether a comment is toxic. 

**Note:** This is an exploratory repo aimed at getting comfortable using these packages. It is for my own learning and by no means a complete project. I will likely be returning to improve it later on!
