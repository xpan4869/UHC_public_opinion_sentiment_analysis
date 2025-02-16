This repository contains data, code, and a video presentation for our MACS 30100 group project, "Machine Learning, Sentiment Analysis, & the United Healthcare CEO Shooting". 
This document will provide a rough overview of the steps we took to complete this project, as well as the documents in this repo that contain the related code and data for each step.
# Data Collection(Hailey):
We downloaded comments from the r/HealthInsurance subreddit using the arctic_shift data dump download tool. 
- raw_data: folder contains .jsonl files with the raw data downloaded from arctic_shift. We downloaded both posts and comments, but ultimately only utilized comments in this project.
*r_healthinsurance_comments.jsonl.zip needs to be unzipped in order to be viewed*
# Data Labeling (Amrita):
Since Supervised Machine Learning models require labeled data, we had to create a labeled dataset ourselves.

Using a stratified sampling method, we selected a random subset of 1,000 comments for hand-labeling, which we then used to train our model.

To ensure consistency: We divided the dataset into four equal sections of 250 comments.

Each of us served as the primary rater for one section and the secondary rater for another.

We used the following labels:

- -1 for negative sentiment
- 0 for neutral sentiment
- 1 for positive sentiment
- -99 for unrelated comments

Once all comments had been labeled twice, we conducted a Cohen’s Kappa test to measure inter-rater agreement. 
Our test returned a score of 0.5, indicating a moderate level of agreement. 
However, disagreements existed for approximately 300 comments, which we manually reviewed and resolved.

# Preprocessing (Hailey):
- preprocessing.ipynb: Jupyter notebook containing the code and output for each preprocessing step undertaken to prepare the text data for the model
- preprocessing: folder contains preprocessed_data.csv.zip, which contains the preprocessed dataset that was ultimately used for testing our model
  *preprocessed_data.csv.zip needs to be unzipped in order to be viewed*
# Model Training (Zixuan) & Model Evaluation & (Yolanda):
- traning_final.ipynb: Jupyter notebook containing the code in training, fine-tuning, and evaluating decision tree model, random forest model, and linear regression model for multiclassification task
# Data Analysis (Yolanda):
- final_data_analysis.ipynb:  Jupyter notebook containing the code and graphs for the shift of sentiments prior and after the UHC CEO shooting event
