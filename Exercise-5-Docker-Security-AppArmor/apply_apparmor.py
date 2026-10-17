
import docker

client = docker.from_env()

print("Checking Docker security support...")

info = client.info()
security_options = info.get("SecurityOptions", [])

print("Docker security options:", security_options)

if any("apparmor" in str(option).lower() for option in security_options):
    print("AppArmor is reported by Docker.")
    print("A custom profile still needs to be loaded and verified.")
else:
    print("AppArmor is not reported by this Docker environment.")
    print("A custom AppArmor profile cannot be confirmed as enforced.")
    print("Do not claim that AppArmor restrictions have been applied.")
