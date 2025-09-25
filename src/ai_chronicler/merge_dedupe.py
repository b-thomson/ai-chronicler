from pathlib import Path
from pprint import pprint
import json

def merge_dedupe(src_dir: Path, out_dir: Path):
    
    master_list = []

    src_dir_path = Path(src_dir)
    for file in src_dir_path.glob("*.json"):
        
        with open(file, mode="r", encoding="utf-8") as file_handle:
            json_obj = json.load(file_handle)
            if isinstance(json_obj, list):
                master_list.extend(json_obj)
    
    keys = set()
    dedup_list = []
    for item in master_list:
        key = (item.get("chat_id"), item.get("msg_id"), item.get("msg_ts"))
        if key not in keys:
            keys.add(key)
            dedup_list.append(item)

    dedup_list.sort(key=lambda x: (x["msg_ts"] is None, x["msg_ts"]))

    out_file = Path(out_dir) / "out.json"
    with open(out_file, mode="w", encoding="utf-8") as out_file_handle:
        json.dump(dedup_list, out_file_handle)

