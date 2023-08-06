# AIS-Oversampler

This is an Oversampler for handling Class Imbalance in Binary Classification tasks. It uses the AISOv algorithm that is based on Artificial Immune Systems.

The oversampler works for binary classification and can be set to use different mathematical modes of operation that alter how the final resampling data is generated. The AISOv algorithm has been tested on a variety of datasets and performs comparably to other common and proven oversampling techniques.

## Installation

The AIS Oversampler requires:
* Python (>= 3)
* Scikit Learn (>= 1.2)
* Pandas (>= 1.4)
## How to use it
This is a simple code example:
```python
from AIS_Oversampler import ArtificialImmuneSystem 

#create an instance of the oversampler
oversample_AIS = ArtificialImmuneSystem.ArtificialImmuneSystem()

#import a dataset
df = pd.read_csv("../datasets/dataset2.csv",index_col=0)

#separate the features and labels
features = df.drop(["5"], axis=1)
label = df.drop(df.columns[0:-1],axis=1)

#Initialize a classfier
randomForest = RandomForestClassifier()

#call the main function AIS_Resample with the required parameters
df_after_oversampling = oversample_AIS.AIS_Resample(features, label, model = randomForest)

#call the main function AIS_Resample with the required parameters and optional parameters
df_after_oversampling = oversample_AIS.AIS_Resample(preparedDF, labels, max_rounds = 50, stopping_cond = 20, model = randomForest ,K_folds = 5,scorer = 'f1',min_change = 0.005, use_lof = False, mutation_rate = 1.0)
```
### Main Function Parameters

Parameter    | Required | Data Type | Purpose 
------------- | ------------- | ------------- | ------------- 
Features | Yes  | A Pandas DataFrame  | Contains normalized, scaled data (with columns being either binary, or floats) with the labels removed.
Labels | Yes  | A Pandas DataFrame  |  Containsthe label data prepared in the same way as the features.
Model | Yes | A scikit learn classifier  | Denotes the model to be used evaluate each population during resampling. Random Forest and Gradient Boosting produced 
Max_rounds | No | Integer (e.g: 50, 100) | The maximum number of rounds/loops that the oversampler will run for
Stopping_cond | No| Integer (e.g: 20, 50) | The amount of rounds without change before stopping the algorithm
K_folds | No| Integer (e.g: 3, 5)| The number of segments used during k-fold cross validation
Scorer | No| A scikit learn scoring function in string format (e.g ‘f1’) | the scoring metric when evaluating a given population
Min_Change | No| Float (e.g: 0.005, 0.001) | The minimum amount of score change (as a float percentage, 0.001 = 0.1%) required to say that a given population has become a distinct population
Use_Lof | No | Boolean)| If set to true, theoversampler will use local outlier factor (an outlier detection method) when evaluating antibody populations. This yields better results but increases the runtime
Mutation_rate | No | Float (e.g: 1.0)| A value that modulates the amount by which antibodies can mutate in a given round

**Note:** Optional Parameters have a default value but should be given a value and fine tuned for optimal results

## How it works

The AISOv algorithm takes in an Imbalanced dataset and preprocesses it to determine how many antibodies to create and the necessary parameters for the other parts of the function. It then creates an Initial antibody population before entering the Main Program Loop. In the loop, the antibody population is mutated, a fitness function and an evaluation function are applied to find the current best antibody population. Once the termination condition for the loop is met, the current best antibody population is returned.
<img width="447" alt="Screen Shot 2023-03-18 at 10 46 58 PM" src="https://user-images.githubusercontent.com/46852000/226150868-fcce1093-ec05-443d-87b4-f1d831f64a48.png">

You can read more about it here: https://docs.google.com/document/d/1JGAjYWz2Wp95ArWZQnXeLTWyc3ArYzahvMBh8H3XbPA/edit?usp=sharing

## About

This algorithm was originally developped by myself, Nikhil Pyndiah alongside my teamates Adam Jansen and Jacob King for our Honours project. Our aim with the project was to create an easy to use oversampling algorithm which could be used as a drop in replacement for other similar oversamplers. 
The original code alongside extensive testing we did can be found in the  [report](https://docs.google.com/document/d/1JGAjYWz2Wp95ArWZQnXeLTWyc3ArYzahvMBh8H3XbPA/edit?usp=sharing) I linked to above and the original code can be found here: https://github.com/nikhil815/Artificial-Immune-System-For-Class-Imbalance
