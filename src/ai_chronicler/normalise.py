from pathlib import Path

def normalise(src_dir: Path, out_dir: Path):
    for path in src_dir.iterdir():
        print(path)          # full path
        print(path.name)     # filename
        print(path.suffix)