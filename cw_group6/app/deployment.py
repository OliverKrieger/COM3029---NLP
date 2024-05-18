import subprocess
from unit_tests.test_playlist import run_tests

if __name__ == "__main__":
    run_tests()
    # if run_tests():
    #     subprocess.Popen(["python", "-m", "flask", "--app", "main", "run", "--debug"], shell=True)