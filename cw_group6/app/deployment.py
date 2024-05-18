import subprocess
from unit_tests.test_runner import run_tests

if __name__ == "__main__":
    run_tests()
    # subprocess.Popen(["yarn", "--cwd", "../visualiser/", "start"], shell=True)