import pandas as pd

def dt():
    df=pd.read_csv("Book12.csv")
    #print(df)
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(df2,df1,test_size=0.3)
    #print(x_test)
    dtc=DecisionTreeClassifier()
    dtc.fit(x_train,y_train.values.ravel())
    # print("Accuracy is:"(dtc.score(x_test,y_test)))
    perc = dtc.score(x_test,y_test)*100
    return round(perc,2)

def lr():
    df=pd.read_csv("Book12.csv")
    #print(df)
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(df2,df1,test_size=0.2)
    #print(x_test)
    lr=LogisticRegression(random_state=0,solver='lbfgs',max_iter=500,multi_class='multinomial')
    lr.fit(x_train,y_train.values.ravel())
    perc = lr.score(x_test,y_test)*100
    return round(perc,2)

def nb():
    df=pd.read_csv("Book12.csv")
    #print(df)
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(df2,df1,test_size=0.3)
    #print(y_test)
    nb=GaussianNB()
    nb.fit(x_train,y_train.values.ravel())
    perc = nb.score(x_test,y_test)*100
    return round(perc,2)

def rf():
    df=pd.read_csv("Book12.csv")
    #print(df)
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(df2,df1,test_size=0.2)
    #print(x_test)
    rnd=RandomForestClassifier(n_estimators=40)
    rnd.fit(x_train,y_train.values.ravel())
    perc = rnd.score(x_test,y_test)*100
    return round(perc,2)

def svm():
    df=pd.read_csv("Book12.csv")
    #print(df)
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.svm import SVC
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(df2,df1,test_size=0.3)
    #print(y_test)
    nb=SVC(gamma='auto')
    nb.fit(x_train,y_train.values.ravel())
    perc = nb.score(x_test,y_test)*100
    return round(perc,2)
