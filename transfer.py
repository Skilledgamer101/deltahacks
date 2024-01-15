import subprocess

git_command = ["git", "push", "origin", "master"]
def send():
    try:
        result = subprocess.run(git_command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True, check = True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}\n{e.stderr}")

send()
