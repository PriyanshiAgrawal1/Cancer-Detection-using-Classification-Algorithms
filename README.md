# Cancer-Detection-using-Classification-Algorithms

It is a known fact that, cancer rates have increased to great heights in the recent times. The only way to completely cure cancer is to detect it's presence at an early stage, for which appropriate diagnosis is available. The main objective of this project is the detection, and classification of cancerous cells in the patients genome expression, on detection of which he/she can be provided rightful treatment. 
In this project we have dealt mainly with two types of cancer: Breast cancer and Prostate cancer in females and males respectively. We have implemented Machine Learning to find out signs of cancer, and what type of cancer, if seen. The reason being, physicians are capable of diagnosing a patient with cancer, with an accuracy of 71%, according to a latest research, on the other hand Machine Learning techniques can show up to 91% accuracy for rightful classification.

Since, the primary focus is to detect and classify the type of cancer in the patient, we have used classification algorithms under Machine learning as Decision Tree, Random Forest, Support Vector Machine, Logistic Regression and Naive Bayes. Effort has been made to identify the best techniques providing the highest accuracy for both the cancers and enhancing them with Stratified K-Fold and dimensionality reduction.


## Getting Started

* [Anaconda 3](https://docs.anaconda.com/anaconda/install/windows/) - An environment so as to isolate different machine learning libraries and versions.
* [Atom Editor](https://atom.io/) - Atom is a free and open-source text and source code editor for macOS, Linux, and Microsoft Windows.

  * Install the following packages inside Atom (Atom Editor > Welcome Guide > Install a Package > Open Installer) :
  
    - platformio-ide-terminal
    - autocomplete-python
    - atom-django
  * Verify, language-python pre-installed (If, you have installed Anaconda3)
  * To create a virtual environment with conda use the following command on the terminal :
    ```
    conda create --name virtual_env_name django
    ```
  * To activate the virtual environment :
    ```
    activate virtual_env_name
    ```
  * To install Django in the Atom Editor : 
    ```
    conda install django
    ```
  * To create a Django project :
    ```
    django-admin startproject project_name
    ```
  * To create a Django app :
    ```
    python manage.py startapp app_name
    ```
  * Install the required dependencies :
    ```
    pip install -r requirements.txt
    ```
* [Django Administration](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/) - Django's database support

  * To activate the database :
    ```
    python manage.py migrate
    python manage.py makemigrations app_name
    python manage.py migrate
    ```
  * To create superuser :
    ```
    python manage.py createsuperuser
    ```
* To run the development server :
    ```
    python manage.py runserver
    ```
    On running the above command, you must see at the end :
    ```
    Django version 1.10.5, using settings 'first_project.settings'
    Starting development server at http://127.0.0.1:8000/
    ```
    
## System Architecture
<p align="center">
 <img src="https://user-images.githubusercontent.com/67894114/86591387-1de5c180-bfaf-11ea-8c42-a2260dc785d9.png" height="500" width="450">
</p>
  
## Methodology

The system is built atop Python3, and has 3 main steps :

#### 1. Collection of Data Samples :
The foremost step, is to collect the data samples. It is a known fact that machine learning models are trained upon the data samples i.e. the examples for the same               attributes. Therefore, having a good clench of the sample data is very essential.
A data set can be divided into two subsets:
  *	Training Dataset – It is a batch of data samples which is used to train the model.
  *	Test Dataset – It is a batch of data samples which is used to test the trained model.

##### Datasets :
  * [Breast Cancer Dataset](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)
  * [Prostate Cancer Dataset](https://www.kaggle.com/sajidsaifi/prostate-cancer)
  
#### 2. Building Classification Models :

Classification is a machine learning method that is used to group the input data into various classes depending on which class it can most relate to. The main purpose of any classification problem is to predict that class under which the new data can fit. So, we have used various classification models, to categorize the cancer as Malignant or Benign. A conclusion is inferred by the classification model from the input values provided to it for training i.e. the training dataset. This conclusion helps the classification model to predict the class labels/categories for the new data i.e. the test dataset.

The classification models built for categorization are :
  * Support Vector Machine
  * Decision Tree
  * Logistic Regression
  * Random Forest
  * Naive Bayes
  
#### 3. Improvement of Classification Models :

Stratified K-Folds and dimensionality reduction are used to improve the classification models, so as to give a better accuracy.

##### Stratified K-Folds

Stratified K-Folds cross-validation technique is a commonly used statistical method used to evaluate the dexterity of machine learning models. It is one of the main applications of machine learning which is used in selection and comparison of various models for a particular predictive modelling scenario. The Stratified K-Folds cross-validator computes indices of train or test data samples to split the data into train or test sets. The folds are made by preserving the percentage of data samples for each category. In our implementation, K-folds from 0 to 20 with a step-size of 5 has been applied.

#### Dimensionality Reduction

Dimensionality reduction is basically a technique where the attributes of the input dataset i.e. random variables can be reduced. This is useful because most of the times, a large number of attributes can lead to the curse of dimensionality which means that more input features can make the prediction task exigent, resulting in poor performance of the machine learning model and hence reduced accuracy. Dimensionality reduction can be either linear or non-linear, based on the technique used. The basic linear technique, which is called Principal Component Analysis (PCA) has been used in this implementation.

## Results 

### 1. Prostate Cancer
![Screenshot (421)](https://user-images.githubusercontent.com/67894114/86590562-7b790e80-bfad-11ea-8d78-b54d62d7f7f2.png)

### 2. Breast Cancer
![Screenshot (422)](https://user-images.githubusercontent.com/67894114/86590597-8f247500-bfad-11ea-90cb-b7c8d9f37839.png)

## Citation

If you use this repository, please use this to cite the paper :
```
@article {  agrawalbreast,
            title={Breast Cancer and Prostate Cancer Detection using Classification Algorithms},
            author={Agrawal, Priyanshi and Deb, Sharmista and Shilpa, AV and Raju, Shirisha N and Sreenivasa, BC}
         }
```

## Authors

* **Priyanshi Agrawal** - [PriyanshiAgrawal1](https://github.com/PriyanshiAgrawal1)
* **Shilpa AV** - [Shilpa-av](https://github.com/Shilpa-av)

