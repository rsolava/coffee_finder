## **Recommending coffee shops in Austin**

### Ryan Solava

#### Abstract
In this project, we leverage Yelp reviews for coffee shops in the Austin
area to create a recommendation system. We use a variety of NLP tools. The
recommender has been deployed as an app through Streamlit.


#### Design
Customers looking for a coffee shop have a variety of needs, and it can
be challenging to find a coffee shop that fits what they are looking for. This
is especially true in areas that are unfamiliar to the person, for example when
on a vacation. A system that could recommend a coffee shop to a person based on
their needs and desires would quite useful. This project does exactly this,
by using review data and NLP tools.

#### Data
The data is a collection of reviews from Yelp. There are 7,616 reviews.
The reviews were considered on a sentence level for the most part, where
each sentence was treated as its own row. There were 58,864 total sentences
in the dataset. The data was originally scraped from Yelp, and download from this
location [here](https://data.world/rdowns26/austin-coffee-yelp-reviews).


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
you can use the recommendation system
[here](https://share.streamlit.io/rsolava/coffee_finder/main) at the
Streamlit app I created.
Also, my code and visualizations are posted to my
[personal GitHub](https://github.com/rsolava/coffee_rec).
