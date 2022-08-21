import os
import json

KERNEL_NAME = os.environ.get('KERNEL_NAME')
KERNEL_JOB_FILE = os.environ.get('KERNEL_JOB_FILE')


def prepare_metadata_file():
  
  with open('kernel-metadata.json', 'r') as f:
    metadata_file = json.load(f)
    
  metadata_file['id'] = '/'.join([metadata_file['id'].split('/')[0], KERNEL_NAME])
  metadata_file['title'] = KERNEL_NAME
  metadata_file['code_file'] = KERNEL_JOB_FILE
  metadata_file['language'] = 'python'
  metadata_file['kernel_type'] = 'script'
  metadata_file['enable_gpu'] = True
  
  with open('kernel-metadata.json', 'w') as f:
    json.dump(metadata_file, f)
    
  
if __name__ == '__main__':
  prepare_metadata_file()

