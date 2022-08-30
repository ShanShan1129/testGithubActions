import os
files = os.listdir('.')
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
print(files_dir)
