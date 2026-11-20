import pickle, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

features=["cgpa","aptitude_score","technical_score","communication_score","internships","projects"]
data=pd.read_csv("dataset.csv")
Xtr,Xte,ytr,yte=train_test_split(data[features],data.placed,test_size=.2,random_state=42,stratify=data.placed)
model=Pipeline([("scale",StandardScaler()),("logistic_regression",LogisticRegression(max_iter=1000,random_state=42))])
model.fit(Xtr,ytr)
pred=model.predict(Xte)
print(f"Test accuracy on the included synthetic dataset: {accuracy_score(yte,pred)*100:.2f}%")
print(classification_report(yte,pred,target_names=["Not Placed","Placed"]))
with open("placement_model.pkl","wb") as f: pickle.dump(model,f)
print("Saved placement_model.pkl")
