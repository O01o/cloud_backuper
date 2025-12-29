import subprocess

def get_tree(path: str) -> str:
    cp = subprocess.run(["tree", path], encoding='utf-8')
    return cp.stdout