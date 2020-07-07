import random
import numpy as np
import os

def test_Prostate(p_csv):
    import pandas as pd
    df=pd.read_csv("Prostate_Cancer.csv")
    csv_path = os.path.join("C:/Users/A V SHILPA/Downloads",p_csv)
    df3 = pd.read_csv(csv_path)
    df1=df[["diagnosis_result"]]
    df2=df.drop("diagnosis_result",1)
    from sklearn.linear_model import LogisticRegression
    test_data=df3.iloc[0]
    test_target=df3.iloc[0]
    lr=LogisticRegression(random_state=0,solver='lbfgs',max_iter=5000,multi_class='multinomial')
    lr = lr.fit(df2, df1.values.ravel())
    prediction=lr.predict([test_data])
    id = int(test_data['ID'])
    radius = test_data['radius']
    texture = test_data['texture']
    perimeter = test_data['perimeter']
    area = test_data['area']
    smoothness = test_data['smoothness']
    compactness = test_data['compactness']
    symmetry = test_data['symmetry']
    fractal_dimension = round(test_data['fractal_dimension'],3)
    if prediction=='B':
        result = "BENIGN"
    else:
        result = "MALIGNANT"
    return result,id,radius,texture,perimeter,area,smoothness,compactness,symmetry,fractal_dimension;

def test_Breast(b_csv):
    import pandas as pd
    df=pd.read_csv("Breast_Cancer.csv")
    df1=df[["diagnosis"]]
    df2=df.drop("diagnosis",1)
    csv_path = os.path.join("C:/Users/A V SHILPA/Downloads",b_csv)
    df3 = pd.read_csv(csv_path)
    from sklearn.ensemble import RandomForestClassifier
    test_data=df3.iloc[0]
    test_target=df3.iloc[0]
    rfc=RandomForestClassifier(n_estimators=50)
    rfc = rfc.fit(df2, df1.values.ravel())
    prediction=rfc.predict([test_data])
    id = int(test_data['id'])
    radius = test_data['radius_mean']
    texture = test_data['texture_mean']
    perimeter = test_data['perimeter_mean']
    area = test_data['area_mean']
    smoothness = test_data['smoothness_mean']
    compactness = test_data['compactness_mean']
    symmetry = test_data['symmetry_mean']
    fractal_dimension = round(test_data['fractal_dimension_mean'],3)
    if prediction=='B':
        result = "BENIGN"
    else:
        result = "MALIGNANT"
    return result,id,radius,texture,perimeter,area,smoothness,compactness,symmetry,fractal_dimension;
