import os
path='.'
files = os.listdir(path)
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
print(files_dir)
print('ログ' not in files_dir)
