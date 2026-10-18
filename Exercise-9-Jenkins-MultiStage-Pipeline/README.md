# Exercise 9: Jenkins Multi-Stage Pipeline

## Objective
Build, test, deploy, and run a Python Flask application using a Jenkins Declarative Pipeline.

## Project Structure
```text
Exercise-9-Jenkins-MultiStage-Pipeline/
├── Jenkinsfile
└── python-flask-app/
    ├── app.py
    ├── requirements.txt
    └── test_app.py
```

## Technologies Used
- Jenkins
- Python
- Flask
- Git and GitHub
- Jenkins Declarative Pipeline

## Pipeline Stages
1. **Build** — Create a Python virtual environment and install dependencies.
2. **Test** — Run unit tests for the Flask application.
3. **Deploy** — Copy the application into a deployment directory.
4. **Run Application** — Start the Flask application.
5. **Test Application** — Send an HTTP request and verify the response.

## Expected Application Response
```text
Hello, Jenkins Multi-Stage Pipeline!
```

## Execution
The pipeline is configured through the `Jenkinsfile`. Run the Jenkins pipeline job and review the console output to verify that all stages complete successfully.

## Screenshots
Screenshots showing the Jenkins pipeline execution and successful test results will be added here after the pipeline runs successfully.
