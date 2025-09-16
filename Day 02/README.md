# A Typical ML project pipeline

This diagram is an overview of how a machine learning project usually works in the real world. 
It’s broken into four main phases — **Planning**, **Data**, **Modeling**, and **Deployment** — and it’s not just a straight line. We will find ourselves looping back, adjusting, and improving things along the way. Here’s what each part really means:

---

# **Frame the Problem (Planning Phase)**

Everything starts here. 
We figure out what problem we're actually trying to solve.
Don't think about the solution, and what success would look like from a business point of view.
We just ask: “Why are we doing this?”

---

# **Work with the Data (Data Phase)**

Once the problem’s clear, we look for and understand, prepare the data that can help solve it.

It consists of the following steps in order:

* **1. Get Data** 
We find and gather the data we need.
For Example: pulling from databases, scraping web data, or requesting access from another team.

* **2. Explore the Data** 
Now we take a good look at what we have got. 
Following information are gained in this step:
    - Are there missing values? 
    - Are there outliers? 
    - Any obvious patterns? 
This is like playing with data to understand what we are working with.

* **3. Prepare the Data**
We clean things up and maybe create new features that will help the model. 
This might mean :
    - converting dates 
    - filling in missing values 
    - combining columns
    - dropping rows/columns that only add noise to the model

* **4. Split the Data** 
As the final step of the phase , we divide our data into training, validation, and test sets.
This is done so that we can train a model on a set of training data, then improve its performance on the validation set and evaluate its performance on the unseen test set.

---

# **Build and Improve the Model (Modeling Phase)**

Now, we actually get into the machine learning part.
This phase consists of the following steps:

* **1. Explore Models** 
Try out different types of models and see what looks promising.

* **2. Fine-Tune** 
We then tweak the best ones to improve performance. 
We can also combine a few models to get even better results.

* **3. Validate and Test** 
We use the test set to get a realistic sense of how our model will do in the real world. 
If it doesn’t perform as expected, we go back to exploring other models.

---

# **Deploy and Monitor (Deployment Phase)**

Once we have got an acceptable model, we make it available to use to intended users following the below steps.

* **1. Present the Solution** 
We share your results with your team or stakeholders and show them how it works, what we learned, and what limitations there are.

* **2. Deploy to Production** 
We put the model into the real world where it starts making predictions on real world data.

* **3. Monitor and Maintain**
Models can get worse over time if the there is change in distribution of input data (data drift) or change in the input-output relationship (concept drift)
We need to watch performance and retrain when necessary.

---

![ML Pipeline image](ML_pipeline.png)