import os
import time
import subprocess
import json

SLEEP_TIME = 5
KERNEL_NAME = os.environ.get('KERNEL_NAME')


def parse_kaggle_output(filename):
    output_str = ''
    with open(f'{filename}.log', 'r') as f:
        json_output = json.load(f)
        for line in json_output:

            output_str += line.get('data')
    
    return output_str

def main():
  while True:
    
    output = subprocess.check_output(['kaggle', 'kernels', 'status', KERNEL_NAME])
    output = output.decode("utf-8")
    print(output)
    if 'error' in output:
      # download outputs in log file
      output = subprocess.check_output(['kaggle', 'kernels', 'output', KERNEL_NAME, '-p', KERNEL_NAME])
      logs = parse_kaggle_output(os.path.join(KERNEL_NAME, KERNEL_NAME))
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
