import os

def get_relative_path(base_path, target_path):
    return os.path.relpath(target_path, base_path)

def create_unique_dir(base_dir, prefix):
    while True:
        rand_str = str(random.randint(1000, 9999))
        dir_path = os.path.join(base_dir, f"{prefix}_{rand_str}")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            return dir_path
