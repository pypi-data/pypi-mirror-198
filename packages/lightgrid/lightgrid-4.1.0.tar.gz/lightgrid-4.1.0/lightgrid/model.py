
import time
import json
import warnings
import random as rd

def R2_score(y_pred, y_val):
    """
    Function to get R2-score
    :param y_pred: predict sequence
    :param y_val: real sequence
    :return: R2_score
    """
    total1 = 0
    for i in range(len(y_val)):
        total1 = total1 + y_val[i]
    total2 = 0
    total3 = 0
    for i in range(len(y_val)):
        total2 = total2 + (y_val[i] - total1/len(y_val)) ** 2
        total3 = total3 + (y_val[i] - y_pred[i]) ** 2
    r2 = 1 - total3/total2
    return r2

def succe_percent(y_pred, y_val):
    """
    Function to get success percent
    :param y_pred: predict sequence
    :param y_val: real sequence
    :return:  success percent
    """
    customCount = 0
    for i in range(len(y_pred)):
        if y_pred[i] == y_val[i]:
            customCount = customCount + 1
    denominator = len(y_pred)
    return (customCount / denominator)

def timer(func):
    """
    Annotation to get  function run time
    :return:  function run time
    """
    def count_time(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('lightgrid run time:{:.5f}s'.format(end_time - start_time))
    return count_time

def ramdon_sample(seed,maxSize,scale):
    """
    Function to get random data index 
    :param seed: random seed
    :param maxSize: data max length
    :scale: train and test data spilt scale
    :return:  test data index ; train data index
    """
    rd.seed(seed)
    res1 = rd.sample(range(0,maxSize),int(maxSize*scale))
    res2 = [elem for elem in  range(0,maxSize) if elem not in res1]
    return res1,res2
    
def paramIterator(dictValues, resList, dictKeys, jude=True):
    """
    Procedure to get dictionary parameter collection
    :param dictValues: dcitionary values list(IN)
    :param dictKeys: dcitionary keys list (IN)
    :param jude: recursive termination condition(IN)
    :param resList:  dictionary parameter collection(OUT)
    """
    if jude: dictValues = [[[i] for i in dictValues[0]]] + dictValues[1:]
    if len(dictValues) > 2:
        for i in dictValues[0]:
            for j in dictValues[1]:
                paramIterator([[i + [j]]] + dictValues[2:], resList, dictKeys, False)
    elif len(dictValues) == 2:
        for i in dictValues[0]:
            for j in dictValues[1]:
                resList.append(dict(zip(dictKeys, i + [j])))

def holdOutValid(function,valid_times,random_seed,scale,optimal_fun,param,data, target):

    model = function(**param)

    sr = 0
    for i in range(valid_times):
        res1,res2 = ramdon_sample(random_seed+i,data.shape[0],scale)
        x_train = data[res2,:]
        y_train = target[res2]
        x_val = data[res1,:]
        y_val = target[res1]
        model.fit(x_train, y_train)
        y_pred = model.predict(x_val)
        sr = sr + globals()[optimal_fun](y_pred, y_val)
    sr = sr/valid_times

    print('[lightgrid]  test dict: ' + str(param) + '  score:' + str(sr))
    
    return sr
    
class lightgrid():

    def __init__(self,
                 function,
                 paramList,
                 n_iter,
                 ):
        
        """auto adjust parameter  . author YSW

        Parameters
        ----------
        :param function: you should input a class name such as : test
        :param optimal_fun: optimal function ,option invoke 'R2_score' or 'succe_percent'
        :param valid_times: valid times
        :param random_seed: random seed
        :param scale: train and test data spilt scale
        :param silent: boolean,Whether to output logs during program operation
        :param save_model: boolean,save model or not

        Examples
        --------
        >>> from sklearn.tree import DecisionTreeClassifier  
        >>> from sklearn.datasets import load_breast_cancer
        >>> import numpy as np
        >>> from sklearn.model_selection import RandomizedSearchCV
        >>> 
        >>> dt = DecisionTreeClassifier()
        >>> param_grid = {
        >>>              'criterion': ['gini','entropy'],
        >>>              'splitter':['best','random'],
        >>>              'max_depth':np.arange(10,200,10),
        >>>              'min_samples_split':np.arange(0.01,0.1,0.01),
        >>>              }
        >>> 
        >>> data = load_breast_cancer()
        >>> x_train = data['data']
        >>> y_train = data['target']
        >>> rand_ser = RandomizedSearchCV(dt,param_grid,n_iter=100)
        >>> rand_ser.fit(x_train,y_train)
        >>> rand_ser.best_params_
        ...                             
        ...
        {'splitter': 'random', 'min_samples_split': 0.08, 'max_depth': 30, 'criterion': 'gini'}
        """

        super(lightgrid, self).__init__()
        self.function = function
        self.n_iter = n_iter
        self.paramList = paramList
        self.bst_param = None
        
 
        
    @timer
    def fit(self, data, target):
        bst_param = {}


        resList = []
        paramIterator(list(self.paramList.values()), resList, list(self.paramList.keys()))

        
        maxsize = len(resList)       # solution upper and lower bounds
        parent = int(maxsize * np.random.rand(1))   # initialization parent id
        N_GENERATIONS = self.n_iter  # loop times
        MUT_STRENGTH = len(resList)    # mutation strength
        
        valid_times = 3 
        random_seed = 10
        train_test_scale = 0.2
        valid_function = 'succe_percent'

        for _ in range(N_GENERATIONS):

            kid = parent + MUT_STRENGTH * np.random.randn(1)  
            kid = int(np.clip(kid, *[0,maxsize-1])) # limit num range

            fp = holdOutValid(self.function,valid_times,random_seed,train_test_scale,valid_function,resList[parent],data, target)
            fk = holdOutValid(self.function,valid_times,random_seed,train_test_scale,valid_function,resList[kid],data, target)

            p_target = 1/5
            if fp < fk:     # kid better than parent
                parent = kid
                ps = 1.     # kid win -> ps = 1 (successful offspring)
            else:
                ps = 0.
            # adjust global mutation strength
            MUT_STRENGTH *= np.exp(1/np.sqrt(2) * (ps - p_target)/(1 - p_target))
        
        self.bst_param = resList[parent]

        print('[lightgrid]  everything is OK')
        return