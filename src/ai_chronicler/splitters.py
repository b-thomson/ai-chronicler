import json
from pathlib import Path
from datetime import datetime
from pprint import pprint
from collections import defaultdict

def split_day(record_list):
       
    out_files = defaultdict(list)

    for record in record_list:
        msg_ts = record.get("msg_ts")
        if msg_ts:
            msg_day_str = datetime.fromtimestamp(msg_ts).strftime("%Y%m%d")
            out_files[msg_day_str].append(record)
            
    return out_files

def split_week(record_list):
    
    out_files = defaultdict(list)

    for record in record_list:
        msg_ts = record.get("msg_ts")
        if msg_ts:
            msg_week_str = datetime.fromtimestamp(msg_ts).strftime("%Y%W")
            out_files[msg_week_str].append(record)
            
    return out_files

def split_month(record_list):

    out_files = defaultdict(list)

    for record in record_list:
        msg_ts = record.get("msg_ts")
        if msg_ts:
            msg_mon_str = datetime.fromtimestamp(msg_ts).strftime("%Y%m")
            out_files[msg_mon_str].append(record)
            
    return out_files

def split_chat(record_list):
    
    out_files = defaultdict(list)

    for record in record_list:
        chat_id = record.get("chat_id")
        if chat_id:
            out_files[chat_id].append(record)
            
    return out_files

handlers = {
        "day": split_day,
        "week": split_week,
        "month": split_month,
        "chat": split_chat
    }

outfile_paths = {
        "day": Path("/Users/benthomson/code/ai-chronicler/data/output/by_day"),
        "week": Path("/Users/benthomson/code/ai-chronicler/data/output/by_week"),
        "month": Path("/Users/benthomson/code/ai-chronicler/data/output/by_month"),
        "chat": Path("/Users/benthomson/code/ai-chronicler/data/output/by_chat")
}

def split(src_dir: Path, mode: str):
    
    src_file = Path(src_dir) / "out.json"
    with open(src_file, mode="r", encoding="utf-8") as src_file_handle:
        json_obj = json.load(src_file_handle)

    record_list = sorted(json_obj, key=lambda x: (x["msg_ts"] is None, x["msg_ts"]))

    outfiles = handlers[mode](record_list)


    for record in outfiles:
    
        outfile_path = (outfile_paths[mode] / record).with_suffix(".json")
        with open(outfile_path, mode="w", encoding="utf-8") as outfile_fh:
            json.dump(outfiles[record], outfile_fh)
    

