# ai-chronicler

A tool to parse and organize ChatGPT export files into clean, searchable Markdown.  
Supports splitting conversations by day, week, month, or chat name.

## Features

- Extracts `converations.json`from zipped chatGPT data exports
- Converts raw JSON into Markdown
- Supports splitting by day, week, month or chat name
- Caches results to stop reprocessing the same zips

## Installation

Clone the repository and set up a virtual environment:
```bash
git clone https://github.com/b-thomson/ai-chronicler.git
cd ai-chronicler
python3 -m venv .venv
source .venv/bin/activate   # On macOS/Linux OR
.venv\Scripts\activate      # On Windows
pip install -r requirements.txt

## Usage

Run the tool from the command line:

```bash
python -m ai_chronicler --help
```

Example commands (planned):

```bash
# Extract conversations into a single Markdown file
python -m ai_chronicler extract --input data/input_zips --output data/output/all.md

# Split conversations by day
python -m ai_chronicler extract --split day

# Split conversations by chat name
python -m ai_chronicler extract --split chat
```