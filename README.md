# ENSF612_GROUP10_REPO
## Extending a README Classifier using an Optimized SVC Pipeline and GridSearch in PySpark <br/>
ENSF612 Term Project Code Repository and Helper Method Storage <br/>
Group Members:
- Tobi Odufeso, M.Eng. Software Engineering
- Zachary Frena, M.Eng. Software Engineering
- Ziryan Seddek, M.Eng. Software Engineering

**Repository Documents Summary**
- `helper_scripts` contains python files used in the data acquisition and preprocessing steps, where:
  * `api-json.py`, `api-parser.py`, and `md-parser.py` were used to pull new samples from the GitHub API and parse MD textual content.
  * `file_rename_and_links.py` was used to properly name the acquired input README's to match the file naming convention required by the READMEClassifier model (during machine learning model replication and feature extraction).
- `READMEClassifier_Model_Replication.ipynb` is the PySpark script (implemented in Databricks x AWS cluster) to replicate/recreate the READMEClassifier performances (on the original dataset) using the SVC, RandomForest, and LogisticRegression Classifiation algorithms, native to SciKitLearn. The model replication on the original dataset resulted in the exact same per-model score. Replicating the papers existing models also enabled us to perform experiments using the original models and methodology on the new and new + old datasets.
- `ENSF612_CODE_Group10.ipynb` is the PySpark program (implemented in U of C TALC cluster), used to extend the READMECLassifier using: Preprocessing, MLPipeline + GridSearch, on an optimized and hyperparameter tuned SVC (Support Vector Classifier - linear).

This is a multiclassification, multilabel problem, that we have broken into 8 binary classification problems (1 for each of the possible target lables/classes). Reference to the original research paper:

*G. A. Prana, C. Treude, F. Thung, T. Atapattu, and D. Lo, “Categorizing the content of github README files,” Empirical Software Engineering, vol. 24, no. 3, pp. 1296–1327, 2018.* 

Available at: https://arxiv.org/pdf/1802.06997.pdf
![image](https://user-images.githubusercontent.com/83628551/146195910-2280ca0a-5eab-4699-8221-1e6716a5525a.png)

