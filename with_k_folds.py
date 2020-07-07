import pandas as pd

def dt_5():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=DecisionTreeClassifier()
        clf.fit(x_train,y_train)
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def dt_10():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=DecisionTreeClassifier()
        clf.fit(x_train,y_train)
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def dt_15():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=DecisionTreeClassifier()
        clf.fit(x_train,y_train)
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def dt_20():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=DecisionTreeClassifier()
        clf.fit(x_train,y_train)
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def lr_5():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=LogisticRegression(solver='lbfgs',max_iter=500,random_state=0,multi_class='multinomial')
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def lr_10():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=LogisticRegression(solver='lbfgs',max_iter=500,random_state=0,multi_class='multinomial')
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def lr_15():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=LogisticRegression(solver='lbfgs',max_iter=500,random_state=0,multi_class='multinomial')
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def lr_20():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=LogisticRegression(solver='lbfgs',max_iter=500,random_state=0,multi_class='multinomial')
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def rf_5():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=RandomForestClassifier(n_estimators=50)
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def rf_10():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=RandomForestClassifier(n_estimators=50)
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def rf_15():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=RandomForestClassifier(n_estimators=50)
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def rf_20():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=RandomForestClassifier(n_estimators=50)
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def nb_5():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=GaussianNB()
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def nb_10():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=GaussianNB()
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def nb_15():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=GaussianNB()
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def nb_20():
    df=pd.read_csv("Book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=GaussianNB()
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)

def svm_5():
    df=pd.read_csv("Book12.csv")
    #print(df)
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=SVC(gamma='auto')
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)
    # print(round(average_score,2))

def svm_10():
    df=pd.read_csv("Book12.csv")
    #print(df)
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=SVC(gamma='auto')
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)
    # print(round(average_score,2))

def svm_15():
    df=pd.read_csv("Book12.csv")
    #print(df)
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=SVC(gamma='auto')
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    return round(average_score,2)
    # print(round(average_score,2))

def svm_20():
    df=pd.read_csv("Book12.csv")
    #print(df)
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    for train_index, test_index in folds.split(df2,df1):
        x_train=df2.iloc[train_index]
        y_train=df1.iloc[train_index]
        x_test=df2.iloc[test_index]
        y_test=df1.iloc[test_index]
        clf=SVC(gamma='auto')
        clf.fit(x_train,y_train.values.ravel())
        print(clf.score(x_test,y_test))
        avg.append(clf.score(x_test,y_test))
    average_score=(sum(avg)/len(avg))*100
    # print("20:",round(average_score,2))
    return round(average_score,2)
