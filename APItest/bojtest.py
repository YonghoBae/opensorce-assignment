import subprocess

def run_boj_init():
    try:
        # boj init 명령어 실행
        command = ['boj', 'init']
        print(f"Executing command: {command}")
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Command output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

# boj init 명령어 실행
run_boj_init()
