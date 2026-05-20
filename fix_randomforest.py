# Fixed code for RandomForestClassifier cell - copy this into your notebook

# Add these imports at the top of the cell
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier

# Check if variables exist and have correct data
try:
    print(f"x_train shape: {x_train.shape}")
    print(f"y_train shape: {y_train.shape}")
    print(f"x_train type: {type(x_train)}")
    print(f"y_train type: {type(y_train)}")
except NameError:
    print("Error: x_train or y_train not defined. Please run the train_test_split cell first.")

#####RandomForestClassifier
pipe = Pipeline([('vect', CountVectorizer()),
                 ('tfidf', TfidfTransformer()),
                 ('model', RandomForestClassifier(random_state=42))])

RandomForestmodel = pipe.fit(x_train, y_train) 
prediction = RandomForestmodel.predict(x_test)
print("accuracy: {}%".format(round(accuracy_score(y_test, prediction)*100,2)))
RandomForestmodel_accuracy = round(accuracy_score(y_test, prediction)*100,2)
