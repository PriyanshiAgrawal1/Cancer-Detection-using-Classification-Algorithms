def svm_5():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        clf=SVC(gamma='auto')
        clf.fit(x_train,y_train.values.ravel())
        one=(clf.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100

def svm_10():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        clf=SVC(gamma='auto')
        clf.fit(x_train,y_train.values.ravel())
        one=(clf.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100

def svm_15():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        clf=SVC(gamma='auto')
        clf.fit(x_train,y_train.values.ravel())
        one=(clf.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100

def svm_20():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        clf=SVC(gamma='auto')
        clf.fit(x_train,y_train.values.ravel())
        one=(clf.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100

def dt_5():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        dtc=DecisionTreeClassifier()
        dtc.fit(x_train,y_train.values.ravel())
        one=(dtc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100


def dt_10():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        dtc=DecisionTreeClassifier()
        dtc.fit(x_train,y_train.values.ravel())
        one=(dtc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100


def dt_15():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        dtc=DecisionTreeClassifier()
        dtc.fit(x_train,y_train.values.ravel())
        one=(dtc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100


def dt_20():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=20)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        dtc=DecisionTreeClassifier()
        dtc.fit(x_train,y_train.values.ravel())
        one=(dtc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100


def lr_5():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        lr=LogisticRegression(solver='lbfgs',max_iter=7000,random_state=0,multi_class='multinomial')
        lr.fit(x_train,y_train.values.ravel())
        one=(lr.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100


def lr_10():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        lr=LogisticRegression(solver='lbfgs',max_iter=7000,random_state=0,multi_class='multinomial')
        lr.fit(x_train,y_train.values.ravel())
        one=(lr.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100


def lr_15():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        lr=LogisticRegression(solver='lbfgs',max_iter=5000,random_state=0,multi_class='multinomial')
        lr.fit(x_train,y_train.values.ravel())
        one=(lr.score(x_test,y_test))
        print(one)
        print('\n')
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100


def lr_20():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        lr=LogisticRegression(solver='lbfgs',max_iter=5000,random_state=0,multi_class='multinomial')
        lr.fit(x_train,y_train.values.ravel())
        one=(lr.score(x_test,y_test))
        print(one)
        print('\n')
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100


def rf_5():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        rfc=RandomForestClassifier(n_estimators=50)
        rfc.fit(x_train,y_train.values.ravel())
        one=(rfc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100


def rf_10():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        rfc=RandomForestClassifier(n_estimators=50)
        rfc.fit(x_train,y_train.values.ravel())
        one=(rfc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100


def rf_15():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        rfc=RandomForestClassifier(n_estimators=50)
        rfc.fit(x_train,y_train.values.ravel())
        one=(rfc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100


def rf_20():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        rfc=RandomForestClassifier(n_estimators=50)
        rfc.fit(x_train,y_train.values.ravel())
        one=(rfc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100


def nb_5():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        dtc=GaussianNB()
        dtc.fit(x_train,y_train.values.ravel())
        one=(dtc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100

def nb_10():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        dtc=GaussianNB()
        dtc.fit(x_train,y_train.values.ravel())
        one=(dtc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100

def nb_15():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        dtc=GaussianNB()
        dtc.fit(x_train,y_train.values.ravel())
        one=(dtc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100

def nb_20():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(df2)
    scaled_data=scalar.transform(df2)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,df1):
        x_train=pca[train_index]
        y_train=df1.iloc[train_index]
        x_test=pca[test_index]
        y_test=df1.iloc[test_index]
        dtc=GaussianNB()
        dtc.fit(x_train,y_train.values.ravel())
        one=(dtc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return round(avg_score,2)*100

def svm():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    df2=df.drop("cancer",1)
    from sklearn.decomposition import PCA
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.preprocessing import StandardScaler
    sclar=StandardScaler()
    sclar.fit(df2)
    scaled_data=sclar.transform(df2)
    hel=PCA(n_components=10)
    hel.fit(scaled_data)
    pca=hel.transform(scaled_data)
    x1_train,x1_test,y1_train,y1_test=train_test_split(pca,df1,test_size=0.3)
    rfc=SVC(gamma='auto')
    rfc.fit(x1_train,y1_train.values.ravel())
    g1=rfc.score(x1_test,y1_test)
    return(round(g1,2))*100

def dt():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    #print(df1)
    df2=df.drop("cancer",1)
    from sklearn.decomposition import PCA
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.preprocessing import StandardScaler
    #brst=load_breast_cancer()

    sclar=StandardScaler()
    sclar.fit(df2)
    scaled_data=sclar.transform(df2)
    #print(scaled_data)
    hel=PCA(n_components=10)
    hel.fit(scaled_data)
    pca=hel.transform(scaled_data)
    #print(pca)
    x1_train,x1_test,y1_train,y1_test=train_test_split(pca,df1,test_size=0.3)
    dtc=DecisionTreeClassifier()
    dtc.fit(x1_train,y1_train.values.ravel())
    g1=dtc.score(x1_test,y1_test)
    return(round(g1,2))*100

def lr():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    #print(df1)
    df2=df.drop("cancer",1)
    from sklearn.decomposition import PCA
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    #brst=load_breast_cancer()

    sclar=StandardScaler()
    sclar.fit(df2)
    scaled_data=sclar.transform(df2)
    #print(scaled_data)
    hel=PCA(n_components=10)
    hel.fit(scaled_data)
    pca=hel.transform(scaled_data)
    #print(pca)
    x1_train,x1_test,y1_train,y1_test=train_test_split(pca,df1,test_size=0.3)
    rfc=LogisticRegression(random_state=0,solver='lbfgs',max_iter=500,multi_class='multinomial')
    rfc.fit(x1_train,y1_train.values.ravel())
    g1=rfc.score(x1_test,y1_test)
    return(round(g1,2))*100


def rf():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    #print(df1)
    df2=df.drop("cancer",1)
    from sklearn.decomposition import PCA
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    #brst=load_breast_cancer()

    sclar=StandardScaler()
    sclar.fit(df2)
    scaled_data=sclar.transform(df2)
    #print(scaled_data)
    hel=PCA(n_components=10)
    hel.fit(scaled_data)
    pca=hel.transform(scaled_data)
    #print(pca)
    x1_train,x1_test,y1_train,y1_test=train_test_split(pca,df1,test_size=0.3)
    rfc=RandomForestClassifier(n_estimators=50)
    rfc.fit(x1_train,y1_train.values.ravel())
    g1=rfc.score(x1_test,y1_test)
    return(round(g1,2))*100


def nb():
    import pandas as pd
    df=pd.read_csv("book12.csv")
    df1=df[["cancer"]]
    #print(df1)
    df2=df.drop("cancer",1)
    from sklearn.decomposition import PCA
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    from sklearn.preprocessing import StandardScaler
    sclar=StandardScaler()
    sclar.fit(df2)
    scaled_data=sclar.transform(df2)
    hel=PCA(n_components=10)
    hel.fit(scaled_data)
    pca=hel.transform(scaled_data)
    x1_train,x1_test,y1_train,y1_test=train_test_split(pca,df1,test_size=0.3)
    rfc=GaussianNB()
    rfc.fit(x1_train,y1_train.values.ravel())
    g1=rfc.score(x1_test,y1_test)
    return(round(g1,2))*100
