
# Exercise 5: Docker Security with AppArmor

## 1. Objective

The objective of this exercise is to explore Docker container security, investigate AppArmor support, use the Docker SDK for Python, and test restricted actions inside a container.

## 2. Technologies Used

- Docker Desktop
- Python 3.11
- Flask
- Docker SDK for Python
- Docker security options

## 3. Project Structure

```text
Exercise-5-Docker-Security-AppArmor/
├── app.py
├── Dockerfile
├── requirements.txt
├── apply_apparmor.py
├── test_restricted_actions.py
└── README.md
```

## 4. Flask Application

The Flask application listens on port 5000 and returns a welcome message when the root URL is accessed.

## 5. Docker Image

Build the image from the Devops Lab directory:

```powershell
docker build -t flask-apparmor .\Exercise-5-Docker-Security-AppArmor
```

Run the container:

```powershell
docker run -d --name flask-apparmor-test -p 5002:5000 flask-apparmor
```

Access the application at:

http://localhost:5002/

## 6. Docker Security Inspection

The Docker security options were checked using:

```powershell
docker info --format '{{json .SecurityOptions}}'
```

Observed output:

```text
["name=seccomp,profile=builtin","name=cgroupns"]
```

The AppArmor kernel parameter was checked from an Ubuntu container:

```powershell
docker run --rm ubuntu:latest sh -c "cat /sys/module/apparmor/parameters/enabled 2>/dev/null || echo 'AppArmor not available in this container environment'"
```

The output was `N`, indicating that AppArmor was not enabled or exposed through this environment.

## 7. Python Docker SDK

The `apply_apparmor.py` script connects to Docker through the Python SDK and checks the security options reported by the Docker daemon.

The script confirmed that AppArmor was not reported by this Docker environment. Therefore, a custom AppArmor profile could not be verified as enforced.

## 8. Restricted Action Tests

The `test_restricted_actions.py` script created a temporary container using the `no-new-privileges:true` security option.

### Test 1: Read `/etc/passwd`

Result: The command succeeded with exit code 0.

### Test 2: Execute a shell command

Result: The command succeeded with exit code 0 and displayed the container's user identity.

### Interpretation

These tests demonstrate that the tested actions were permitted. The `no-new-privileges` option is not equivalent to an AppArmor policy and does not, by itself, block reading `/etc/passwd` or running a shell.

## 9. Limitation

The project was developed using Docker Desktop on Windows. The current Docker environment did not report AppArmor support, and the kernel parameter check returned `N`.

Consequently, custom AppArmor enforcement and AppArmor-based denial tests could not be demonstrated in this environment. These results must not be interpreted as proof that AppArmor restrictions were applied.

To complete the AppArmor-specific portion, the profile must be loaded and tested in a suitable Linux environment with AppArmor enabled and supported by its Docker daemon.

## 10. Conclusion

This exercise demonstrated how to build and run a Flask application in Docker, inspect Docker security options using the Python SDK, and test container actions. It also identified an environment limitation preventing verification of custom AppArmor enforcement.
