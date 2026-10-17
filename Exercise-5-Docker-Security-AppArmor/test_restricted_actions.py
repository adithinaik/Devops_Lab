
import docker

client = docker.from_env()

container = None

try:
    print("Starting security test container...")

    container = client.containers.run(
        "flask-apparmor",
        detach=True,
        ports={"5000/tcp": 5003},
        name="flask-security-test",
        security_opt=["no-new-privileges:true"],
    )

    print("Container started:", container.name)

    print("\nTest 1: Read /etc/passwd")
    exit_code, output = container.exec_run("cat /etc/passwd")
    print("Exit code:", exit_code)
    print(output.decode(errors="replace"))

    print("\nTest 2: Try to run a shell")
    exit_code, output = container.exec_run("sh -c 'id'")
    print("Exit code:", exit_code)
    print(output.decode(errors="replace"))

    print(
        "\nNote: These tests do not prove AppArmor restrictions. "
        "This container uses Docker's no-new-privileges option instead."
    )

finally:
    if container is not None:
        container.remove(force=True)
        print("\nTest container removed.")
