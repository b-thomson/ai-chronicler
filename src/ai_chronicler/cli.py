import argparse
from extract import extract


def main():
    parser = argparse.ArgumentParser(description="Extract conversations.json from zipped ChatGPT exports")
    parser.add_argument("src_dir", help = "Source directory for the data export .zip files")
    parser.add_argument("out_dir", help = "Target directory to write the extracted conversations.json files")
    args = parser.parse_args()

    print(f"Extracting from {args.src_dir} → {args.out_dir}")
    extract(src_dir=args.src_dir,out_dir=args.out_dir)

if __name__ == "__main__":
    main()