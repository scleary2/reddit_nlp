## Executive Summary:

Overview: Natural Language Processing (NLP) is a form of Machine Learning that uses tokenization, lemmatization, and stemming to classify and extract sentiment from text. There are many other applications of NLP that are outside the scope of this project.

Problem Statement: Can a classification model using posts from two subreddits accurately identify which category a post belongs to?

Data: I will be using 4,000 posts each from the r/wallstreetbets and r/MachineLearning. My feature variables will consist solely of the Title of each individual post and the target will be which subreddit the post originated from.

Modeling: I am going to be utilizing CountVectorizer and TfidfVectorizer to perform tokenization on my text in addition to MultinomialNB and SVC as my modeling algorithms. The most efficient way to do this will be through the use of a pipeline so that I can feed data directly through my model without having to make manual adjustments.

Results: An optimized SVC model utilizing TfidfVectorizer with stop_words removed was my best performing model. It was able to accurately classify which subreddit a post belonged to a little over 96% of the time on the testing data. In addition, the model appears to be misclassifying each subreddit at a similar rate of just under 5% and 4%. For demonstration purposes, I have created a basic web app to host my model so that you can see the model working effectively. I would put this model into use with confidence that it will classify the majority of posts correctly.

Next Steps: Incorporate sentiment analysis and add it to my text. I believe model performance could be increased further with sentiment analysis because the model should do a better job of picking up on underlying semantics/meaning. Additionally, I am going to run this data through a RNN with the intent of increasing model performance. 


### Contents:

- [Import Data](#Read-in-Data)
- [NB TfidfVectorizer](#NB-TfidfVectorizer)
- [NB Tfidf No Stop Words](#NB-Tfidf-No-Stop-Words)
- [Multinomial NB](#Multinomial-NB-CV)
- [SVC Tfidf](#SVC-Tfidf)
- [Optimal SVC](#Optimal-SVC)
- [Optimal SVC Word Counts and Weights](#Optimal-SVC-Word-Counts-and-Weights)
- [Pickle](#Pickle)