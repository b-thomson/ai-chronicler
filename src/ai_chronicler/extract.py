import os
from pathlib import Path
import zipfile

file_ext = ".zip"
conv_file = "conversations.json"

def extract(zip_dir: Path, output_dir: Path):
    
    for zip_file in os.listdir(zip_dir):

        if zip_file.endswith(file_ext):
            zip_file_stem = Path(zip_file).stem
            source_file_path = os.path.join(zip_dir,zip_file)

            with zipfile.ZipFile(source_file_path) as zf:
                zf.extract(conv_file, output_dir)
            
            rename_source = os.path.join(output_dir,conv_file)
            rename_target = os.path.join(output_dir,f"{zip_file_stem}_{conv_file}")
            os.rename(rename_source,rename_target)
