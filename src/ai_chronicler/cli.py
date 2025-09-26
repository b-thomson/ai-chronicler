import argparse
import tomllib
from pathlib import Path

from .extract import extract
from .normalise import normalise
from .merge_dedupe import merge_dedupe
from .splitters import split

def load_config(path="ai_chronicler.toml"):
    with open(path, "rb") as f:
        return tomllib.load(f)



def main():
    config = load_config()
    parser = argparse.ArgumentParser(description="Extract conversations.json from zipped ChatGPT exports")
    parser.add_argument("--src_dir", type = Path, help = "Source directory for the data export .zip files")
    parser.add_argument("--extr_dir", type = Path, help = "Target directory to write the extracted conversations.json files")
    parser.add_argument("--norm_dir", type = Path, help = "Target directory to write the normalised conversations.json files")
    parser.add_argument("--merge_dir", type = Path, help = "Target directory to write the merged, normalised JSON file to")
    parser.add_argument("--out_dir", type = Path, help = "Target directory to write the output Markdown file(s) to")
    parser.add_argument("--mode", choices=["day","week","month","chat","user"], help = "Splitter configuration method, eg: --day, --week, --month, --chat")
    args = parser.parse_args()

    src_dir = args.src_dir or Path(config["paths"]["input_dir"])
    extr_dir = args.extr_dir or Path(config["paths"]["extracted_dir"])
    norm_dir = args.norm_dir or Path(config["paths"]["normalised_dir"])
    merge_dir = args.merge_dir or Path(config["paths"]["merge_dir"])

    out_dir = args.out_dir or Path(config["splitters"][args.mode])

    print(f"Extracting from {src_dir} → {extr_dir}")
    extract(src_dir=src_dir,out_dir=extr_dir)

    print(f"Normalising JSON files in {extr_dir}")
    normalise(src_dir=extr_dir,out_dir=norm_dir)

    print(f"Merging and deduplication of JSON files in {norm_dir}")
    merge_dedupe(src_dir=norm_dir,out_dir=merge_dir)
   
    print(f"Splitting and writing JSON files by {args.mode} to {out_dir}")
    split(src_dir=merge_dir,mode=args.mode)

if __name__ == "__main__":
    main()