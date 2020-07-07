def svm_5():
    from sklearn.datasets import load_breast_cancer
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=5)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=SVC(gamma='auto')
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100


def svm_10():
    from sklearn.datasets import load_breast_cancer
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=10)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=SVC(gamma='auto')
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def svm_15():
    from sklearn.datasets import load_breast_cancer
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=15)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=SVC(gamma='auto')
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def svm_20():
    from sklearn.datasets import load_breast_cancer
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=20)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=SVC(gamma='auto')
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def dt_5():
    from sklearn.datasets import load_breast_cancer
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=5)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=DecisionTreeClassifier()
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def dt_10():
    from sklearn.datasets import load_breast_cancer
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=10)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=DecisionTreeClassifier()
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def dt_15():
    from sklearn.datasets import load_breast_cancer
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=15)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=DecisionTreeClassifier()
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def dt_20():
    from sklearn.datasets import load_breast_cancer
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=20)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=DecisionTreeClassifier()
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100


def lr_5():
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=5)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=LogisticRegression(solver='lbfgs',max_iter=7000,random_state=0,multi_class='multinomial')
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def lr_10():
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=10)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=LogisticRegression(solver='lbfgs',max_iter=7000,random_state=0,multi_class='multinomial')
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def lr_15():
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=15)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=LogisticRegression(solver='lbfgs',max_iter=7000,random_state=0,multi_class='multinomial')
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def lr_20():
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=20)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=LogisticRegression(solver='lbfgs',max_iter=7000,random_state=0,multi_class='multinomial')
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def rf_5():
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=5)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=RandomForestClassifier(n_estimators=50)
        clf.fit(x_train,y_train)
        # print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    # print("\n THE ARRAY OF AVERAGE SCORE IS :\n",avg)
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def rf_10():
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=10)
    breast=load_breast_cancer()
    #print(folds)
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        #print(train_index)
        #print ('...........')
        #print(test_index)
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=RandomForestClassifier(n_estimators=50)
        clf.fit(x_train,y_train)
        avg.append(clf.score(x_test,y_test))
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def rf_15():
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=15)
    breast=load_breast_cancer()
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=RandomForestClassifier(n_estimators=50)
        clf.fit(x_train,y_train)
        avg.append(clf.score(x_test,y_test))
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def rf_20():
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=20)
    breast=load_breast_cancer()
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=RandomForestClassifier(n_estimators=50)
        clf.fit(x_train,y_train)
        avg.append(clf.score(x_test,y_test))
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def nb_5():
    from sklearn.datasets import load_breast_cancer
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=5)
    breast=load_breast_cancer()
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=GaussianNB()
        clf.fit(x_train,y_train)
        avg.append(clf.score(x_test,y_test))
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def nb_10():
    from sklearn.datasets import load_breast_cancer
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=10)
    breast=load_breast_cancer()
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=GaussianNB()
        clf.fit(x_train,y_train)
        avg.append(clf.score(x_test,y_test))
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def nb_15():
    from sklearn.datasets import load_breast_cancer
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=15)
    breast=load_breast_cancer()
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=GaussianNB()
        clf.fit(x_train,y_train)
        avg.append(clf.score(x_test,y_test))
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100

def nb_20():
    from sklearn.datasets import load_breast_cancer
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=20)
    breast=load_breast_cancer()
    avg=[]
    for train_index, test_index in folds.split(breast.data,breast.target):
        x_train=breast.data[train_index]
        y_train=breast.target[train_index]
        x_test=breast.data[test_index]
        y_test=breast.target[test_index]
        clf=GaussianNB()
        clf.fit(x_train,y_train)
        avg.append(clf.score(x_test,y_test))
    average_score=sum(avg)/len(avg)
    return round(average_score,2)*100
