import subprocess
from unit_tests.test_runner import run_tests

if __name__ == "__main__":
    if run_tests():
        subprocess.Popen(["python", "-m", "flask", "--app", "main", "run", "--debug"], shell=True)