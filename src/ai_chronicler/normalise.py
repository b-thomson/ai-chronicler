import json
from pathlib import Path


def walk_json(conversation_id, conversation_title, mapping_dict, message_id):

    out = []
    message_dict = mapping_dict[message_id]
    message = message_dict.get("message")
    if message:
        parts = message.get("content").get("parts")
        if parts:
            msg_id = message_dict["message"]["id"]
            msg_ts = message_dict["message"]["create_time"]
            msg_speaker = message_dict["message"]["author"]["role"]
            msg = message_dict["message"]["content"]["parts"]
            record = {
                "chat_id": conversation_id,
                "chat_title": conversation_title,
                "msg_id": msg_id,
                "msg_ts": msg_ts,
                "msg_speaker": msg_speaker,
                "msg": msg,
            }

            out.append(record)

    if message_dict["children"]:
        for child in message_dict["children"]:
            out.extend(walk_json(conversation_id, conversation_title, mapping_dict, child))

    return out


def normalise(src_dir: Path, out_dir: Path):

    for path in src_dir.glob("*.json"):

        out = []

        with open(path, mode="r", encoding="utf-8") as read_file:

            json_obj = json.load(read_file)
            for item in json_obj:

                mapping_root_key = None
                for k, v in item["mapping"].items():
                    if v["parent"] is None:
                        mapping_root_key = k
                        break

                message_list = walk_json(item["conversation_id"], item["title"], item["mapping"], mapping_root_key)
                out.extend(message_list)

        out_path = out_dir / path.name
        with open(out_path, mode="w", encoding="utf-8") as write_file:
            json.dump(out, write_file)
