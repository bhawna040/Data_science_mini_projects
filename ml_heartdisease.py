# 1.Library 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib #Model saving
from ucimlrepo import fetch_ucirepo #Fetching dataset
from imblearn.over_sampling import SMOTE #Handling imbalanced data
#2 Data Imports
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score

print(" Libraries imported successfully.")

# ye fetch kar raha ha dataset from UCI repository
heart_disease = fetch_ucirepo(id=45)
X_data = heart_disease.data.features
y_data = heart_disease.data.targets

# Ye combine kar raha ha ek single dataframe main
df = pd.concat([X_data, y_data], axis=1)
print("\n 2. Data Imported Successfully from UCI Repository")

# 3. & 4. Data Cleaning and Preprocessing
print("\n 3. & 4. Starting Data Cleaning and Preprocessing")

# Handle missing values by filling with the median
for col in df.columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].median())
print("Missing values filled.")

# Create a binary 'HeartDisease' target column (0 = No Disease, 1 = Yes)
df['HeartDisease'] = (df['num'] > 0).astype(int)
df = df.drop('num', axis=1)
print("Binary target column 'HeartDisease' created.")

# Replace 0 values in 'chol' (ye cholesterol level hai) with the median
median_chol = df['chol'][df['chol'] != 0].median()
df['chol'] = df['chol'].replace(0, median_chol)
print("Cleaned 'chol' column.")

# 5. Feature Engineering (Encoding)
print("\n 5. Performing Feature Engineering (One-Hot Encoding)")
categorical_cols = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal']
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True) # Converts categorical columns into numeric format for ML.
print("Categorical features encoded.")

# 6. & 7. Feature/Target Split and Train/Test Split
print("\n 6. & 7. Splitting Data")
X = df_encoded.drop('HeartDisease', axis=1)
y = df_encoded['HeartDisease']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Training set: {X_train.shape[0]} samples | Testing set: {X_test.shape[0]} samples")

# 8. Data Balancing (SMOTE)
print("\n 8. Balancing Training Data with SMOTE")
smote = SMOTE(random_state=42)
X_train_sm, y_train_sm = smote.fit_resample(X_train, y_train) #equal kar raha hai (matble 80-20 ko 50-50 kar raha hai)

# 9. Feature Scaling
print("\n 9. Scaling Features")
scaler = StandardScaler() #Ye sare features ko same scale main kar deta hai (mean=0, std=1) for better work.
X_train_scaled = scaler.fit_transform(X_train_sm)
X_test_scaled = scaler.transform(X_test)

# 10. & 11. Model Selection and Evaluation
print("\n 10. & 11. Training and Evaluating Baseline Models")
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42)
}

# Store results for comparison plot
model_performance = []

for name, model in models.items():
    model.fit(X_train_scaled, y_train_sm)
    y_pred = model.predict(X_test_scaled)
    
    # Store performance metrics
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    model_performance.append({'Model': name, 'Accuracy': accuracy, 'F1 Score': f1})
    
    print(f"\n--- {name} Performance ---")
    print(classification_report(y_test, y_pred))
# Convert performance list to a DataFrame for easy plotting
performance_df = pd.DataFrame(model_performance)

# 12. Feature Importance
print("\n 12. Calculating Feature Importance")
#Use the baseline Random Forest model for feature importance calculation
rf_model = models['Random Forest']
importances = rf_model.feature_importances_
feature_names = X.columns

feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
print("Top 5 most important features:\n", feature_importance_df.head())

# 13. Final Model Tuning (Hyperparameter Tuning)
print("\n 13. Tuning the Random Forest Model with GridSearchCV")
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5],
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='f1_weighted',
    n_jobs=-1,
)

grid_search.fit(X_train_scaled, y_train_sm)
best_rf = grid_search.best_estimator_
print("Best Parameters found:", grid_search.best_params_)


# 14. Saving the Model (Optional for Deployment)
print("\n 14. Saving Final Model and Scaler for Deployment")
joblib.dump(best_rf, 'heart_disease_model.joblib')
joblib.dump(scaler, 'scaler.joblib')
print("Model saved as 'heart_disease_model.joblib'")
print("Scaler saved as 'scaler.joblib'")

# 15. Visualization of Results
print("\n 15. Generating Final Visualizations")

# Set plot style
sns.set_style("whitegrid")
plt.figure(figsize=(20, 5))

# Plot 1: Compare multiple model performances side-by-side
plt.subplot(1, 3, 1)
sns.barplot(x='Model', y='F1 Score', data=performance_df, hue='Model', palette='viridis', legend=False)
plt.title('Baseline Model F1 Scores Comparison')
plt.xticks(rotation=15)

# Plot 2: Visualize feature importance
plt.subplot(1, 3, 2)
sns.barplot(x='Importance', y='Feature', data=feature_importance_df.head(10), hue='Feature', palette='plasma', legend=False)
plt.title('Top 10 Feature Importances')

# Plot 3: Plot confusion matrix for the final tuned model
y_pred_tuned = best_rf.predict(X_test_scaled)
cm = confusion_matrix(y_test, y_pred_tuned)
plt.subplot(1, 3, 3)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['No Disease', 'Heart Disease'],
            yticklabels=['No Disease', 'Heart Disease'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix (Tuned Model)')

plt.tight_layout()
plt.show()