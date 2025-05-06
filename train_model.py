import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib


df_train = pd.read_csv("data/csv_result-KDDTrain+.csv")
df_test = pd.read_csv("data/csv_result-KDDTest+.csv")

df_train.drop(['id'],axis=1,inplace=True)
df_test.drop(['id'],axis=1,inplace=True)

for col in df_train.select_dtypes(include='object'):
    df_train[col] = LabelEncoder().fit_transform(df_train[col])

for col in df_test.select_dtypes(include='object'):
    df_test[col] = LabelEncoder().fit_transform(df_test[col])  

X = df_train.drop("'class'", axis=1)
y = df_train["'class'"]


clf = RandomForestClassifier(n_estimators=100)
clf.fit()

print("Classification Report:\n", classification_report(df_test["'class'"], clf.predict(df_test.drop("'class'", axis=1))))

joblib.dump(clf,'ids_model.pkl')
