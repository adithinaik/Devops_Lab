# Exercise 7: Jenkins CI Automation

## Objective
To understand Continuous Integration (CI) and configure a Jenkins pipeline that verifies Python availability, runs automated unit tests, and executes a Python application.

## Technologies Used
- Jenkins
- Docker
- Python
- Git and GitHub
- Python unittest

## Project Structure
```text
Exercise-7-Jenkins-CI/
├── app.py
├── test_app.py
├── Jenkinsfile
└── README.md
```

## Application
The Python application contains a `greet()` function that returns a greeting message.

## Automated Testing
The `test_app.py` file contains two unit tests:
1. Verifies the greeting for `DevOps`.
2. Verifies the greeting for another name.

Run the tests locally using:

```powershell
python -m unittest -v test_app.py
```

## Jenkins Pipeline Stages
1. **Checkout** — Begins the CI workflow.
2. **Verify Python** — Checks Python availability.
3. **Run Automated Tests** — Executes the unit tests.
4. **Run Application** — Runs the Python application.
5. **Post Actions** — Reports pipeline success or failure.

## Expected Results
- Python is available in the Jenkins build environment.
- Both unit tests pass.
- The application prints its greeting.
- Jenkins reports the pipeline status.

## Learning Outcomes
- Understand Continuous Integration.
- Create a declarative Jenkins pipeline.
- Automate Python tests.
- Inspect pipeline results in Jenkins.

