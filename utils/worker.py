import os
import time
import subprocess
from parser import parse_kaggle_output

SLEEP_TIME = 5
GIT_REPO_NAME = os.environ.get('REPO_NAME').split('/')[-1]

def main():
  while True:
    
    output = subprocess.check_output(['kaggle', 'kernels', 'status', GIT_REPO_NAME])
    output = output.decode("utf-8")
    print(output)
    if 'error' in output:
      # download outputs in log file
      output = subprocess.check_output(['kaggle', 'kernels', 'output', GIT_REPO_NAME, '-p', GIT_REPO_NAME])
      logs = parse_kaggle_output(os.path.join(GIT_REPO_NAME, GIT_REPO_NAME))
      raise Exception(f'FAIL: Test(s) failed. Full logs below:\n\n{logs}')
    elif 'complete' in output:
      print('SUCCESS: Kaggle Integration Tests')
      break
    elif 'cancel' in output:
      raise Exception(f'FAIL: Test(s) failed. The kaggle kenerl has been canceled')
    else:
      time.sleep(SLEEP_TIME)

if __name__ == '__main__':
  main()
