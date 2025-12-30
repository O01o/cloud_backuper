import subprocess

def get_tree(path: str) -> str:
    cp = subprocess.run(["tree", path], capture_output=True, text=True, encoding='utf-8')
    return cp.stdout