# Features
**Logging:** Enable Flask logging to facilitate log aggregation and querying
**Storage:** Store predictions with a case number for later outcome joining
**MLFlow:** Track experiments using MLFlow to easily reproduce results
**Testing:** Implement both unit and integration testing to ensure model correctness
**Prediction:** Enable point prediction for individual instances
**Error Handling:** Implement robust error handling for unexpected edge cases
**Batch Prediction:** Implement batch prediction for handling large amounts of data
**CI/CD:** Integration with a CI/CD pipeline for automated testing and deployment
**Monitoring:** Implementation of a monitoring solution to track model performance in production
**Explainability:** Support for model explainability, such as SHAP values or LIME
**Feedback Loop:** Implement a feedback loop to continuously retrain and improve the model over time
**Data Catalog:** Integration with a data catalog or data lineage tool to track the source and lineage of the data used in the model
**Version Control:** Implement a version control system to track changes to the model and its associated code and documentation


# RUN Docker Image
docker run -p 8080:8080 ml-deployment-dev


# Test predictions
curl -d '{"Age": 28, "Fare": 7.8958, "Sex": "female", "Embarked": "S"}' -H "Content-Type: application/json" -X POST http://localhost:8080/predict
