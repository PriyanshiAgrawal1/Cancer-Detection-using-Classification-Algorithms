def svm():
    from sklearn.datasets import load_breast_cancer
    from sklearn.svm import SVC
    from sklearn.model_selection import train_test_split
    breast=load_breast_cancer()
    x_train,x_test,y_train,y_test=train_test_split(breast.data,breast.target,test_size=0.3)
    #print(y_test)
    nb=SVC(gamma='auto')
    nb.fit(x_train,y_train)
    return round((nb.score(x_test,y_test)),2)*100

def dt():
    from sklearn.datasets import load_breast_cancer
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    breast=load_breast_cancer()
    x_train,x_test,y_train,y_test=train_test_split(breast.data,breast.target,test_size=0.3)
    #print(x_test)
    dtc=DecisionTreeClassifier()
    dtc.fit(x_train,y_train)
    return round((dtc.score(x_test,y_test)),2)*100

def lr():
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    breast=load_breast_cancer()
    x_train,x_test,y_train,y_test=train_test_split(breast.data,breast.target,test_size=0.2)
    lr=LogisticRegression(random_state=0,solver='lbfgs',max_iter=7000,multi_class='multinomial')
    lr.fit(x_train,y_train)
    return round((lr.score(x_test,y_test)),2)*100

def rf():
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    breast=load_breast_cancer()
    x_train,x_test,y_train,y_test=train_test_split(breast.data,breast.target,test_size=0.2)
    #print(x_test)
    rnd=RandomForestClassifier(n_estimators=40)
    rnd.fit(x_train,y_train)
    return round((rnd.score(x_test,y_test)),2)*100

def nb():
    from sklearn.datasets import load_breast_cancer
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import train_test_split
    breast=load_breast_cancer()
    x_train,x_test,y_train,y_test=train_test_split(breast.data,breast.target,test_size=0.3)
    #print(y_test)
    nb=GaussianNB()
    nb.fit(x_train,y_train)
    return round((nb.score(x_test,y_test)),2)*100
