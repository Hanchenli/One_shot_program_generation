$_$: Load video dataset pickle file from "netflix_session.pkl" as netflix_file, out:netflix_file
$_$: Load video dataset pickle file from "video_dataset.pkl" as video_file, out:video_file

$_$: The dataset contains video resolutions that are not valid. Remove entries in the netflix_file column "resolution" not in [280, 360, 480, 720, 1080]. output:filtered_netflix
$_$: The dataset contains video resolutions that are not valid. Remove entries in the video_file column "resolution" not in [280, 360, 480, 720, 1080]. output:filtered_video


#Here is the python integrated
removed_features = ["absolute_timestamp", "home_id", "index", "session_id", "video_id", "video_position"]

import re
# Function to rename the columns based on the pattern
def rename_columns(col_name):
    if re.match(r'L\d_', col_name):
        return col_name[3:]
    return col_name

# Rename columns
filtered_video.columns = [rename_columns(col) for col in filtered_video.columns]

filtered_video.drop(columns=removed_features, inplace=True)
filtered_netflix.drop(columns=removed_features, inplace=True)

$_$: Use filtered_video to prepare data to use other features to predict the "resolution" field, perform a train-test split on your data. let the test data of features be named X_test, test data of resolution called y_test. output: X_test, y_test
$_$: Then train the model with training dataset. Let the model be named "classifer". output: classifier
$_$: Predict with classifier and X_test, let prediction be called y_pred. output: y_pred


from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, roc_auc_score, roc_curve
import numpy as np
import matplotlib.pyplot as plt
accuracy = accuracy_score(y_true, y_pred)
print("Accuracy:", accuracy)