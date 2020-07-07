def nb_5():
    from sklearn.datasets import load_breast_cancer
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=5)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        gnb=GaussianNB()
        gnb.fit(x_train,y_train)
        one=(gnb.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)

def nb_10():
    from sklearn.datasets import load_breast_cancer
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        gnb=GaussianNB()
        gnb.fit(x_train,y_train)
        one=(gnb.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)

def nb_15():
    from sklearn.datasets import load_breast_cancer
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=15)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        gnb=GaussianNB()
        gnb.fit(x_train,y_train)
        one=(gnb.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)

def nb_20():
    from sklearn.datasets import load_breast_cancer
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=20)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        gnb=GaussianNB()
        gnb.fit(x_train,y_train)
        one=(gnb.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)

def lr_5():
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=5)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        lr=LogisticRegression(solver='lbfgs',max_iter=7000,random_state=0,multi_class='multinomial')
        lr.fit(x_train,y_train)
        one=(lr.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def lr_10():
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        lr=LogisticRegression(solver='lbfgs',max_iter=7000,random_state=0,multi_class='multinomial')
        lr.fit(x_train,y_train)
        one=(lr.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def lr_15():
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=15)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        lr=LogisticRegression(solver='lbfgs',max_iter=7000,random_state=0,multi_class='multinomial')
        lr.fit(x_train,y_train)
        one=(lr.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def lr_20():
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=20)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        lr=LogisticRegression(solver='lbfgs',max_iter=7000,random_state=0,multi_class='multinomial')
        lr.fit(x_train,y_train)
        one=(lr.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def dt_5():
    from sklearn.datasets import load_breast_cancer
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=5)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        dtc=DecisionTreeClassifier()
        dtc.fit(x_train,y_train)
        one=(dtc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def dt_10():
    from sklearn.datasets import load_breast_cancer
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        dtc=DecisionTreeClassifier()
        dtc.fit(x_train,y_train)
        one=(dtc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def dt_15():
    from sklearn.datasets import load_breast_cancer
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=15)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        dtc=DecisionTreeClassifier()
        dtc.fit(x_train,y_train)
        one=(dtc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def dt_20():
    from sklearn.datasets import load_breast_cancer
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=20)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        dtc=DecisionTreeClassifier()
        dtc.fit(x_train,y_train)
        one=(dtc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def rf_5():
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=5)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        rfc=RandomForestClassifier(n_estimators=50)
        rfc.fit(x_train,y_train)
        one=(rfc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)

def rf_10():
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        rfc=RandomForestClassifier(n_estimators=50)
        rfc.fit(x_train,y_train)
        one=(rfc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def rf_15():
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=15)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        rfc=RandomForestClassifier(n_estimators=50)
        rfc.fit(x_train,y_train)
        one=(rfc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def rf_20():
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=20)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        rfc=RandomForestClassifier(n_estimators=50)
        rfc.fit(x_train,y_train)
        one=(rfc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def svm_5():
    from sklearn.datasets import load_breast_cancer
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=5)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=5)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        svc=SVC(gamma='auto')
        svc.fit(x_train,y_train)
        one=(svc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def svm_10():
    from sklearn.datasets import load_breast_cancer
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=10)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=10)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        svc=SVC(gamma='auto')
        svc.fit(x_train,y_train)
        one=(svc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def svm_15():
    from sklearn.datasets import load_breast_cancer
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=15)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=15)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        svc=SVC(gamma='auto')
        svc.fit(x_train,y_train)
        one=(svc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)


def svm_20():
    from sklearn.datasets import load_breast_cancer
    from sklearn.svm import SVC
    from sklearn.model_selection import StratifiedKFold
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    breast=load_breast_cancer()
    folds=StratifiedKFold(n_splits=20)
    avg=[]
    scalar=StandardScaler()
    scalar.fit(breast.data)
    scaled_data=scalar.transform(breast.data)
    new=PCA(n_components=20)
    new.fit(scaled_data)
    pca=new.transform(scaled_data)
    for train_index,test_index in folds.split(pca,breast.target):
        x_train=pca[train_index]
        y_train=breast.target[train_index]
        x_test=pca[test_index]
        y_test=breast.target[test_index]
        svc=SVC(gamma='auto')
        svc.fit(x_train,y_train)
        one=(svc.score(x_test,y_test))
        avg.append(one)
    avg_score=sum(avg)/len(avg)
    return(round(avg_score,2)*100)

def svm():
    from sklearn.datasets import load_breast_cancer
    from sklearn.decomposition import PCA
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.preprocessing import StandardScaler
    brst=load_breast_cancer()
    sclar=StandardScaler()
    sclar.fit(brst.data)
    scaled_data=sclar.transform(brst.data)
    #print(scaled_data)
    hel=PCA(n_components=5)
    hel.fit(scaled_data)
    pca=hel.transform(scaled_data)
    #print(pca)
    x1_train,x1_test,y1_train,y1_test=train_test_split(pca,brst.target,test_size=0.3)
    svc=SVC(gamma='auto')
    svc.fit(x1_train,y1_train)
    g1=svc.score(x1_test,y1_test)
    # print('THE SCORE AFTER REDUCTION')
    return(round(g1,2))*100

def dt():
    from sklearn.datasets import load_breast_cancer
    from sklearn.decomposition import PCA
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.preprocessing import StandardScaler
    brst=load_breast_cancer()
    sclar=StandardScaler()
    sclar.fit(brst.data)
    scaled_data=sclar.transform(brst.data)
    #print(scaled_data)
    hel=PCA(n_components=5)
    hel.fit(scaled_data)
    pca=hel.transform(scaled_data)
    #print(pca)
    x1_train,x1_test,y1_train,y1_test=train_test_split(pca,brst.target,test_size=0.3)
    dtc=DecisionTreeClassifier()
    dtc.fit(x1_train,y1_train)
    g1=dtc.score(x1_test,y1_test)
    # print('THE SCORE AFTER REDUCTION')
    return(round(g1,2))*100

def lr():
    from sklearn.datasets import load_breast_cancer
    from sklearn.decomposition import PCA
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    brst=load_breast_cancer()
    sclar=StandardScaler()
    sclar.fit(brst.data)
    scaled_data=sclar.transform(brst.data)
    #print(scaled_data)
    hel=PCA(n_components=5)
    hel.fit(scaled_data)
    pca=hel.transform(scaled_data)
    #print(pca)
    x1_train,x1_test,y1_train,y1_test=train_test_split(pca,brst.target,test_size=0.3)
    lr=LogisticRegression(random_state=0,solver='lbfgs',max_iter=7000,multi_class='multinomial')
    lr.fit(x1_train,y1_train)
    g1=lr.score(x1_test,y1_test)
    # print('THE SCORE AFTER REDUCTION')
    return(round(g1,2))*100

def rf():
    from sklearn.datasets import load_breast_cancer
    from sklearn.decomposition import PCA
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    brst=load_breast_cancer()
    sclar=StandardScaler()
    sclar.fit(brst.data)
    scaled_data=sclar.transform(brst.data)
    #print(scaled_data)
    hel=PCA(n_components=5)
    hel.fit(scaled_data)
    pca=hel.transform(scaled_data)
    #print(pca)
    x1_train,x1_test,y1_train,y1_test=train_test_split(pca,brst.target,test_size=0.3)
    clf1=RandomForestClassifier(n_estimators=50)
    clf1.fit(x1_train,y1_train)
    g1=clf1.score(x1_test,y1_test)
    return(round(g1,2))*100

def nb():
    from sklearn.datasets import load_breast_cancer
    from sklearn.decomposition import PCA
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    from sklearn.preprocessing import StandardScaler
    brst=load_breast_cancer()

    sclar=StandardScaler()
    sclar.fit(brst.data)
    scaled_data=sclar.transform(brst.data)
    #print(scaled_data)
    hel=PCA(n_components=5)
    hel.fit(scaled_data)
    pca=hel.transform(scaled_data)
    #print(pca)
    x1_train,x1_test,y1_train,y1_test=train_test_split(pca,brst.target,test_size=0.3)
    gnb=GaussianNB()
    gnb.fit(x1_train,y1_train)
    g1=gnb.score(x1_test,y1_test)
    return(round(g1,2))*100
