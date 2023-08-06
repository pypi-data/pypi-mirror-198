import pandas as pd;
import random;
from statistics import fmean, stdev;

from sklearn.model_selection import KFold
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor

class ArtificialImmuneSystem():
    
        
    #TODO Gaussian generation can be optimized by altering how the loops work, putting the col loop on the outside and pre-generated fmean, stdev for the col
            #Currently it generates those values for every antibody
            

    def get_bounds(self, minorityDF) -> dict:
        out = {}
        for col in minorityDF:
            colMax = minorityDF[col].max()
            colMin = minorityDF[col].min()
            out[col] = (colMin, colMax)
        return out

    ####### extractMinorityClass ################
    
    def extractBinaryMinorityClass(self, preparedFeatures, labels) -> pd.DataFrame:
        #preparedFeatures is the dataframe of features, labels is the dataframe of labels
        #returns a dataframe of the minority class
        #get counts of each class from labels
        for col in labels:
                counts = labels[col].value_counts()
                #get the minority class
                minorityLabel = counts.idxmin()

        minorityClass = labels[labels == minorityLabel]
        minorityClass = minorityClass.dropna()
        minorityClass = minorityClass.index.values
        minorityClass = preparedFeatures.loc[minorityClass]
        minorityClass[labels.columns[0]]=minorityLabel
        return minorityClass

    def getBinaryColumns(self, df) -> list:
        return list(df.columns[df.nunique() == 2])

    ####### Creation ################
    # minorityDF - dataframe containing the minority class
    # totalPopulation - The total number of antibodies to create
    # weightingFunction - Can choose between uniform, triangular, ...
    # mode - for use with a triangular function - set to the percentage of the range you wish to be most represented (between 0.0 and 1.0)
    def Creation(self, minorityDF, totalPopulation : int, binaryColumns : list, weightingFunction : str = "uniform", mode : float = 0.5): 
        
        if(minorityDF.isnull().values.any()):
            raise ValueError("Minority Class DataFrame contains NaN")
        
        population = [] #Initializing the empty population
        if mode < 0.0 or mode > 1:
            raise Exception("mode must be between float value between 0.0 and 1.0")
        
        if weightingFunction not in ('uniform', 'triangular', 'gaussian'):
            raise Exception("Unknown function chosen, please use one of 'uniform', 'triangular', or 'gaussian'")

        bounds = self.get_bounds(minorityDF)
        
        if weightingFunction in ["uniform", "triangular"]: #If Generating via uniform or triangular distribution, loop through bounds of columns
            for i in range(totalPopulation): #For every antibody to be created

                antibody = [] #Initializing a single antibody
                for key,bnd in bounds.items(): #Iterate through the columns/dimensions/features of the minority class for each antibody 
                    if key in binaryColumns:
                        antibody += [random.randint(int(bnd[0]),int(bnd[1]))]
                    else:
                        if weightingFunction == "uniform":
                            antibody += [round(random.uniform(bnd[0],bnd[1]),4)] #Add a random value between the lower and upper bounds to the antibody

                        elif (weightingFunction == "triangular"):
                            
                            tri_tip = ( ((bnd[1]-bnd[0]) * mode) + bnd[0] ) #multiplying the difference by the percentage, plus the low bound gives us the point between the two, but percentile

                            if tri_tip < bnd[0]: #Error checks to make sure that the emphasized point isn't outside the bounds
                                tri_tip = bnd[0]
                            elif tri_tip > bnd[1]:
                                tri_tip = bnd[1]

                            antibody += [round( random.triangular(bnd[0],bnd[1], tri_tip), 5)]

                population+=[antibody] #add the created antibody to the population

        elif (weightingFunction == 'gaussian'): #If Generating via Gaussian, loop through columns of dataframe

            for i in range(totalPopulation): #For every antibody to be created

                antibody = [] #Initializing a single antibody
                for bnd in minorityDF: #Iterate over columns in the dataframe
                    values = minorityDF[bnd].tolist() #convert series to list
                    if bnd in binaryColumns:
                        antibody += [random.randint(bounds[bnd][0],bounds[bnd][1])]
                    else:
                        antibody += [round(random.gauss(fmean(values) , stdev(values)), 5)] #using median and stdeviation of values, radomize over gauss

            
                population+=[antibody] #add the created antibody to the population

                
        popDF = pd.DataFrame(population, columns = minorityDF.columns.values)
        return popDF, bounds


    ####### Fitness ################
    #Original features, original labels are the original df before any oversampling
    #Population_features, population_labels are the generated population we want to evaluate
    #Here scorer has to be a function that takes y_pred, y_true and returns a score, not implemented yet
    def fitnessBasic(self, model, original_features, original_labels, population_features, population_labels):

        #TODO:train test split makes train set smaller, we should sample the population based on he difference of the majority class and minority class in origin_feat_train
        origin_feat_train, origin_feat_test, origin_labels_train, origin_labels_test = train_test_split(original_features, original_labels, test_size=0.33)
        
        train_features = pd.concat([origin_feat_train, population_features],ignore_index=True)
        train_labels = pd.concat([origin_labels_train, population_labels],ignore_index=True)

        model.fit(train_features, train_labels.values.ravel())
        predictions = model.predict(origin_feat_test)

        #need more params?
        #TODO:hard coded f1_score, find a way to pass in function for scoring?
        score = f1_score(origin_labels_test.values.ravel(), predictions)
        return score

    #Original features, original labels are the original df before any oversampling
    #Population_features, population_labels are the generated population we want to evaluate
    #Here scorer has to be a function that takes y_pred, y_true and returns a score, not implemented yet
    def fitnessCV(self, model, label, original_df, population_features, population_labels, scorer, iterations):
        
        kf = KFold(n_splits=iterations)
        score = 0 
        for train,test in kf.split(original_df):

            origin_train = original_df.iloc[train]
            origin_test =  original_df.iloc[test]

            origin_feat_train, origin_labels_train = self.separate_df(origin_train, label)
            origin_feat_test, origin_labels_test = self.separate_df(origin_test, label)

            train_features = pd.concat([origin_feat_train, population_features],ignore_index=True)
            train_labels = pd.concat([origin_labels_train, population_labels],ignore_index=True)

            model.fit(train_features, train_labels.values.ravel())
            predictions = model.predict(origin_feat_test)

            #need more params?
            #TODO:hard coded f1_score, find a way to pass in function for scoring?
            score += f1_score(origin_labels_test.values.ravel(), predictions)
        
        return (score/iterations)

    ####### Mutation ################
    def mutatePopulation (self, antiPopulation, bounds, binaryColumns : list, mutationRate : float = 1.0):
        #antiPopulation is the population of antibodies to be mutated
        #bounds is a dictionary of the bounds of each column in the population
        #binaryColumns is a list of the columns that are binary
        #mutationRate denotes how much the antibodies can mutate each round, 1.0 is the default, 0.0 is no mutation, 2.0 is double mutation rate
        #returns a new mutated population of antibodies
        antiPopulation = antiPopulation.copy()
        for col in antiPopulation:
            if bounds[col][0] == bounds[col][1]:
                continue
            elif col in binaryColumns: #Binary Columns must be handled differently than continuous
                
                antiPopulation[col] = antiPopulation[col].map(lambda x : (random.randint(0,1)))
            else:
                bnd_range = (bounds[col][1] - bounds[col][0])*mutationRate #total range of bounds is high - low

                #Setting the low and high bounds to be centered around 0
                hi_bnd = bnd_range/2 
                low_bnd = (0-bnd_range/2)

                #print("Low bound around 0 = " + str(low_bnd) +"| Hi bnd around 0 = "+ str(hi_bnd))
                #print(round(random.uniform(low_bnd,hi_bnd),4))

                antiPopulation[col] = antiPopulation[col].map(lambda x : x+round(random.uniform(low_bnd,hi_bnd),4))
            
        return antiPopulation
    
    #takes a population, generates its LOF score, ranks the data by it and splits it into n_blocks groups of similar data
    def lof(self, original_df, population, n_neighbor:int = 20, n_blocks:int = 4):

        size = len(original_df.index)

        df = pd.concat([original_df,population],ignore_index=True)
        lof = LocalOutlierFactor(n_neighbors = n_neighbor)
        
        y_pred = lof.fit_predict(df)
        X_scores = lof.negative_outlier_factor_

        df["lof"]=X_scores
        population_with_lof = population.copy()
        population_with_lof["lof"] = X_scores[size:]

        population_with_lof = population_with_lof.sort_values(by = ['lof'], ignore_index=True)
        population_with_lof = population_with_lof.drop(columns=['lof'])

        sizeof_block = int(len(population_with_lof.index)/n_blocks)
        i = 0 
        j = int(0)
        result = []
        
        while(i < n_blocks):
            k = int(j+ sizeof_block)
            p = population_with_lof.iloc[j:k]
            result.append(p)
            #result.append(population[j:k])
            j+=sizeof_block
            i+=1
        

        return result

    def get_best_population(self,df, antibody_population, previous_result, label, model, K_folds, scorer):

        result = self.lof(df, antibody_population)

        p1 = pd.concat([result[0],result[1],result[2],previous_result[3]],ignore_index=True)
        p1_features, p1_labels = self.separate_df(p1, label_col=label)
        p1_score = self.fitnessCV(model, label, df, p1_features, p1_labels, scorer, K_folds)

        p2 = pd.concat([result[0],previous_result[1],result[2],result[3]],ignore_index=True)
        p2_features, p2_labels = self.separate_df(p2, label_col=label)
        p2_score = self.fitnessCV(model, label, df, p2_features, p2_labels, scorer, K_folds)

        p3 = pd.concat([result[0],result[1],previous_result[2],result[3]],ignore_index=True)
        p3_features, p3_labels = self.separate_df(p3, label_col=label)
        p3_score = self.fitnessCV(model, label, df, p3_features, p3_labels, scorer, K_folds)

        p4 = pd.concat([previous_result[0],result[1],result[2],result[3]],ignore_index=True)
        p4_features, p4_labels = self.separate_df(p4, label_col=label)
        p4_score = self.fitnessCV(model, label, df, p4_features, p4_labels, scorer, K_folds)

        scores = [p1_score,p2_score,p3_score,p4_score]
        max_score = max(scores)

        if(max_score == p1_score):
            return p1, p1_score
            
        if(max_score == p2_score):
            return p2, p2_score

        if(max_score == p3_score):
            return p3, p3_score
        
        if(max_score == p4_score):
            return p4, p4_score
    
    def comparePopulations(self,population1, population2, labels1, labels2, estimator, iterations, scorer, min_change = 0.005):
        score1 = fmean(self.fitness(estimator, population1, labels1.values.ravel(), iterations, scorer))
        score2 = fmean(self.fitness(estimator, population2, labels2.values.ravel(), iterations, scorer))

        if abs(score1 - score2) < min_change:
            return False
        elif (score1>score2):
            return False
        else:
            return True

    #takes in the previous population's score, will need to add variable in AIS to track this from previous round
    # original features and original labels are the original df split into features and labels
    # population features and population labels are the population df split into features and labels, this is the new population we mutated this round
    # estimator, iterations, scorer not changed from old compare populaitons
    def comparePopulationsCV(self, prev_score, label, original_df, population_features, population_labels, estimator, iterations, scorer, min_change = 0.005):
        score1 = prev_score
        score2 = self.fitnessCV(estimator, label, original_df, population_features, population_labels, scorer, iterations)
        
        if (score2 - score1) >= min_change:
            return True, score2
        else:
            return False, score1



    def comparePopulationsBasic(self, prev_score, original_features, original_labels, population_features, population_labels, estimator, iterations=-1, scorer='', min_change = 0.005):
        score1 = prev_score
        score2 = self.fitnessBasic(estimator, original_features, original_labels, population_features, population_labels)

        if (score2 - score1) >= min_change:
            return True, score2
        else:
            return False, score1

        
    def comparePopulations_lof( self, population_score, old_score, min_change):

        if (population_score - old_score) >= min_change:
            return True, population_score
        else:
            return False, old_score

    
    #separate a df into features and labels
    def separate_df(self, df, label_col):

        columns = df.columns.to_list()
        columns_drop = columns.pop(columns.index(label_col))

        labels = df.drop(columns, axis=1)
        features = df.drop(columns_drop, axis=1)

        return features, labels

    #minorityDF      - the minority dataframe
    #df              - the original dataframe
    #max_rounds      - the maximum number of rounds(loops) of AIS 
    #stopping_cond   - the number of rounds without significant changes to accuracy before stopping the function
    #totalPopulation - the number of elements we want to add to the minority class
    #model           - the model to be used to evaluate the dataset during AIS
    #K-folds         - the number of segments for k-fold cross validation
    #scorer          - the scoring metric when evaluating the dataset

    def AIS(self, minorityDF, df, label, max_rounds, stopping_cond, totalPopulation, model, K_folds, scorer,  min_change : float = 0.005, use_lof : bool = False, mutation_rate : float = 1.0):

        #add code to find binary columns for creation
        binaryColumns = self.getBinaryColumns(minorityDF)

        current_population, bounds = self.Creation(minorityDF,totalPopulation,binaryColumns, weightingFunction='uniform')
        
        count = 0
        no_change = 0

        #created population split into features and labels
        current_gen, current_labels = self.separate_df(current_population, label_col=label)
        current_score = self.fitnessCV(model,label, df, current_gen, current_labels, scorer, K_folds)

        if(use_lof==False):
            while( (count < max_rounds) and (no_change < stopping_cond) ):
                count+=1

                bounds = self.get_bounds(current_population)
                antibody_population = self.mutatePopulation(current_population,bounds,binaryColumns, mutation_rate)
                next_gen, next_labels = self.separate_df(antibody_population, label_col=label)
                change_flg, score = self.comparePopulationsCV(current_score, label, df, next_gen, next_labels, model, K_folds, scorer, min_change)
                
                if (change_flg):
                    no_change = 0
                    current_population = antibody_population.copy()

                    
                else:
                    no_change+=1
                    
                current_score = score #Score will only change if the new population is better than the old population
        
        else:
            
            current_population_lof = self.lof(df, current_population)
            while( (count < max_rounds) and (no_change < stopping_cond) ):
                count+=1

                bounds = self.get_bounds(current_population)
                antibody_population = self.mutatePopulation(current_population,bounds,binaryColumns, mutation_rate)
                best_population, best_population_score = self.get_best_population(df, antibody_population, current_population_lof, label, model, K_folds, scorer)
                change_flg, score = self.comparePopulations_lof(best_population_score, current_score, min_change)

                if (change_flg):
                    no_change = 0

                    current_population = best_population.copy()
                    current_population_lof = self.lof( df, current_population)
                    
                else:
                    no_change+=1

                    
                current_score = score #Score will only change if the new population is better than the old population

        return current_population, count

    def AIS_Resample(self, features, labels, max_rounds, stopping_cond, model, K_folds, scorer = 'f1', min_change = 0.003, use_lof = False, mutation_rate : float = 1.0):
        #features is the dataframe of features, labels is the dataframe of labels
        minorityDF = self.extractBinaryMinorityClass(features, labels)
        
        #features + Labels = the overall Population
        overallPopulation = pd.concat([features,labels],axis=1)
        #The number of elements we want to add to the minority class
        requiredPopulation = len(overallPopulation) - (len(minorityDF)*2)
        
        oversamples,_ = self.AIS(minorityDF,overallPopulation,labels.columns, max_rounds,stopping_cond,requiredPopulation,model,K_folds,scorer, min_change, use_lof, mutation_rate = mutation_rate)
        concatDF = pd.concat([overallPopulation,oversamples],ignore_index=True)
        return (self.separate_df(concatDF, labels.columns[0]))
        

