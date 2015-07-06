# Diskoveror-ML-Server

This is the server for Diskoveror Text Analytics Engine.

## Topic Extraction

   The Basic Idea:

We use these Word2Vec vectors to form clusters by feeding the desired topics to be learnt as seeds to the model, we      follow a unique approach in performing the clustering, that ultimately leads to the formation of clusters that           capture the semantics of any topic fed into it.
    
    
    USPs of our model,
   *  It is capable of predicting topics based on the context in which a word/phrase of the text occurs.
      *   Example,
         1. Text 1: The number of by-products derived from cow’s milk is just unbelievable.
         2. Text 2: All the products sold by Flipkart are of high quality.
      *    Our model is capable of determining that Text 1 is about FOOD Products and Text 2 is about any GENERAL product            based on the context of the sentence.
   *  It is equipped to learn any number of topics and the best part is you could specify what topics it needs to learn        and categorize any given document into.
      *   Example,
         1.  You could specify that you want to learn 2 topics, say, Sports and Technology and the model will train                 itself for these two categories/topics and later the trained model could be used to predict to which topic              any wild document could come under.
         2.  You could specify that you want to learn 2 topics, say, Sports and Technology and the model will train                 itself for these two categories/topics and later the trained model could be used to predict to which topic              any wild document could come under.
         3.  The model has also been crafted in a way that, it does not learn all the noisy topics from the text,                   meticulous evaluations are done before we tag the text under any topic (The algorithms that we use to                  achieve this is our secret recipe), thus ensuring the accuracy of the model.
         4.  We do analysis at both coarse and finer levels of topics, thus enabling our model to be bang on when it                does a prediction.
             *     We currently have a set of 22 coarse topics that in turn have 750+ finer topics contained in them.                     Eg. Music is a coarse topic and Jazz, Pop, Melody, etc are finer topics.
*** The Working:
    
   ![System Architecture](/Topic Model Work Flow.jpg "System Architechture")
