# Exercise 8 — Hello World Jenkins Job

## Objective
To create and execute a Jenkins Freestyle job that retrieves a shell script from GitHub and runs it successfully.

## Tools Used
- Jenkins
- Git and GitHub
- Bash Shell

## GitHub Repository
[devops-sample-code](https://github.com/adithinaik/devops-sample-code)

## Shell Script
The `hello-world.sh` script contains:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

## Jenkins Job Configuration
- **Job Name:** HelloWorld
- **Job Type:** Freestyle project
- **Source Code Management:** Git
- **Repository URL:** `https://github.com/adithinaik/devops-sample-code.git`
- **Build Step:** Execute shell
- **Command:** `sh hello-world.sh`

## Execution Result
The Jenkins job successfully cloned the GitHub repository, executed the shell script, and printed:

```text
Hello, Jenkins!
Finished: SUCCESS
```

## Screenshot
The successful Jenkins Console Output is saved in the `Screenshots` folder.
