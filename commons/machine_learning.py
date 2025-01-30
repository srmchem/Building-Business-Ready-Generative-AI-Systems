# Implemented in Chapter05
# Implementing a Decision Tree for bounded variable predictions
import pandas as pd
import random
from sklearn.preprocessing import LabelEncoder  # For encoding categorical variables
from sklearn.tree import DecisionTreeClassifier  # For training the Decision Tree model
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

# Implemented in Chapter05
import pandas as pd
import random
from sklearn.preprocessing import LabelEncoder  # For encoding categorical variables
from sklearn.tree import DecisionTreeClassifier  # For training the Decision Tree model

def ml_agent(feature1_value, feature2_column):
    # Load the dataset
    df = pd.read_csv("customer_activities.csv")

    # Encode categorical variables
    le_location = LabelEncoder()
    le_activity = LabelEncoder()

    df["LOCATION_ENCODED"] = le_location.fit_transform(df["LOCATION"])
    df["ACTIVITY_ENCODED"] = le_activity.fit_transform(df["ACTIVITY"])

    # Select default location if feature1_value is empty
    if not feature1_value.strip():  # If empty string or only spaces
        feature1_value = df["LOCATION"].mode()[0]  # Most common location

    # Prepare features and target
    X = df[["LOCATION_ENCODED"]]
    y = df["ACTIVITY_ENCODED"]

    # Train a Decision Tree classifier
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)

    # Encode the feature1 value for prediction
    feature1_encoded = le_location.transform([feature1_value])[0]

    # Predict the most probable activity
    predicted_activity_encoded = model.predict([[feature1_encoded]])[0]
    predicted_activity = le_activity.inverse_transform([predicted_activity_encoded])[0]

    # Generate output text
    text = (f"The customers liked the {predicted_activity} because it reminded them of how "
            f"our democracies were born and how it works today. "
            f"They would like more activities during their trips that provide insights into "
            f"the past to understand our lives.")

    return text
