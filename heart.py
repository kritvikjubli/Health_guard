age1 =Element("age")
sex1 =Element("sex")
cp1 =Element("chest_pain")
trestbps1 =Element("trestbps")
chol1 =Element("chol")
fbs1 =Element("fbs")
restecg1 =Element("restecg")
thalach1 =Element("thalach")
exang1 =Element("exang")
oldpeak1 =Element("oldpeak")
slope1 =Element("slope")
ca1 =Element("ca")
thal1 =Element("thal")    

def on_click(*args , **kwargs):
     age2=int(age1.element.value)
     sex2=int(sex1.element.value)
     if(age2<0):
         pyscript.write("result","Age is Invalid")
         return
     if(sex2!=0 and sex2!=1):
         pyscript.write("result","please enter either 0 or 1")
         return
    #  import regex
    #  import smtplib
     import pandas as pd
     from sklearn.model_selection import train_test_split
     from sklearn.linear_model import LogisticRegression
     from sklearn.metrics import accuracy_score
     
    #  if(email1):
    #    emailRegex =regex.compile( r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    #    if(emailRegex.match(email1)):
    #       valid=1


   #   from sklearn.tree import DecisionTreeClassifier

     column_names = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"]
     data = pd.read_csv("./heart.csv", names=column_names)

     X = data.drop("target", axis=1)
     y = data["target"]

     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
     logreg_model = LogisticRegression()
     logreg_model.fit(X_train, y_train)
     
     y_pred = logreg_model.predict(X_test)
   #   tree = DecisionTreeClassifier()
   #   tree.fit(X_train, y_train)
   #   y_pred = tree.predict(X_test)
     def predict_heart_disease_risk():

         age = age1.element.value
         sex = sex1.element.value
         cp = cp1.element.value
         trestbps = trestbps1.element.value
         chol = chol1.element.value
         fbs = fbs1.element.value
         restecg = restecg1.element.value
         thalach = thalach1.element.value
         exang = exang1.element.value
         oldpeak = oldpeak1.element.value
         slope = slope1.element.value
         ca = ca1.element.value
         thal = thal1.element.value

         user_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],columns=X.columns)

         prediction = logreg_model.predict(user_data)
         # prediction = tree.predict(user_data)

         return prediction[0]

     user_prediction = predict_heart_disease_risk()
     accuracy = round(accuracy_score(y_test, y_pred)*100,2)

     if user_prediction == 0:
        pyscript.write("result","Low risk of heart disease.")
     else:
        pyscript.write("result","High risk of heart disease.")
     pyscript.write("accuracy",f"accuracy {accuracy}")
    #  if(valid==1):
    #   s = smtplib.SMTP('smtp.gmail.com', 465)
    #   s.starttls()
    #   s.login("hsharrykj@gmail.com", "shbrnzvywdovazgf")
    #   message = "Message_you_need_to_send"
    #   s.sendmail("hsharrykj@gmail.com", email1, message)
    #   s.quit()

        
