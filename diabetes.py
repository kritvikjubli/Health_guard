preg1=Element("preg")
glu1=Element("glu")
bp1=Element("bp")
skin1=Element("skin")
ins1=Element("ins")
bmi1=Element("bmi")
fun1=Element("fun")
age1=Element("age")

def on_click(*args , **kwargs):
     import pandas as pd
     from sklearn.model_selection import train_test_split
     from sklearn.linear_model import LogisticRegression
     from sklearn.metrics import accuracy_score

     column_names = ["preg","glu","bp","skin","ins","bmi","fun","age","target"]
     data = pd.read_csv("./diabetes.csv", names=column_names)

     X = data.drop("target", axis=1)
     y = data["target"]

     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
     logreg_model = LogisticRegression()
     logreg_model.fit(X_train, y_train)
     y_pred = logreg_model.predict(X_test)
     def dia():

         preg = preg1.element.value
         glu = glu1.element.value
         bp = bp1.element.value
         skin = skin1.element.value
         ins = ins1.element.value
         bmi = bmi1.element.value
         fun = fun1.element.value
         age = age1.element.value

         user_data = pd.DataFrame([[preg,glu,bp,skin,ins,bmi,fun,age]],columns=X.columns)

         prediction = logreg_model.predict(user_data)

         return prediction[0]

     user_prediction = dia()
     accuracy = round(accuracy_score(y_test, y_pred)*100,2)

     if user_prediction == 0:
        pyscript.write("result","Low risk of Diabetes.")
     else:
        pyscript.write("result","High risk of Diabetes.")
     pyscript.write("accuracy",f"Accuracy {accuracy}")

        
