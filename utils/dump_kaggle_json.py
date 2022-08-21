import json, os

kaggle_key = os.environ.get('KAGGLE_KEY')
kaggle_username = os.environ.get('KAGGLE_USERNAME')
kaggle_json = {'username': kaggle_username, 'key': kaggle_key}

with open('.kaggle/kaggle.json', 'w') as f:
    json.dump(kaggle_json, f)