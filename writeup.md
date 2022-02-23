## **Recommending coffee shops in Austin**

### Ryan Solava

#### Abstract



#### Design


#### Data
The data is a collection of reviews from Yelp. There are 7,616 reviews.
The reviews were considered on a sentence level for the most part, where
each sentence was treated as its own row. There were 58,864 total sentences
in the dataset. The data was originally scraped from Yelp, and download from this
location [here](htts://xkcd.com).


#### Algorithms

* CountVectorizer and TFIDF were both tested for creating the document term
matrix
* LSA, NMD, and LDA were all considered for matrix decomposition and dimensionality
reduction
* Cosine distance was used for comparison and in the recommender system

#### Tools

* **Python, Pandas, and Numpy** for standard data science tools
* **sklearn** for CountVectorizer and matrix decomposition algorithms
* **spaCy** for lemmatization
* **VADER** for sentiment analysis
* **NLTK** for stemming and tokenizing
* **Streamlit** for create a web app


#### Communication

A summary of my project and results can be found on my slides. In addition,
you can use the recommendation system [here](https://xkcd.com) at the
Streamlit app I created.
Also, my code and visualizations are posted to my
[personal GitHub](https://github.com/rsolava/coffee_rec).
