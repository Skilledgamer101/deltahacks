import subprocess

git_command = [["git", "add", "."], ["git", "commit", "-m", "added file"], ["git", "push", "origin", "test"]]
def send(command):
    try:
        result = subprocess.run(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True, check = True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}\n{e.stderr}")

for command in git_command:
	send(command)
