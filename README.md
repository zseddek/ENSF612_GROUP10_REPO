# ENSF612_GROUP10_REPO
## Extending a README Classifier using and Optimized SVC Classifier Pipeline in PySpark
ENSF612 Term Project Code Repository and Helper Method Storage

**Repository Documents Summary**
- `helper_scripts` python files used in the data acquisition and preprocessing steps, where:
  * `api-json.py`, `api-parser.py`, and `md-parser.py` were used to pull new samples from the GitHub API and parse MD textual content.
  * `file_rename_and_links.py` was used to properly name the acquired input README's to match the file names required by the READMEClassifier model (during machine learning model replication and feature extraction).
- `READMEClassifier_Model_Replication.ipynb` is the PySpark script (implemented in Databricks x AWS cluster) to replicate/recreate the READMEClassifier performances using the SVC, RandomForest, and LogisticRegression Classifiation algorithms, native to SciKitLearn.
- `ENSF612_CODE_Group10.ipynb` is the PySpark program (implemented in U of C TALC cluster), used to extend the READMECLassifier using: Preprocessing, MLPipeline + GridSearch, on an optimized and hyperparameter tuned SVC (Support Vector Classifier - linear).
