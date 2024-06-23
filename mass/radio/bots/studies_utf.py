import sys
import os
import json
from pathlib import Path
from newapi import printe

main_dir = Path(__file__).parent.parent

studies_urls_to_files_dir = Path("/data/project/ncc/nccbot/studies_urls_to_files")
# ---
if not os.path.exists(studies_urls_to_files_dir):
    studies_urls_to_files_dir = Path("I:/ncc/nccbot/studies_urls_to_files")
    print(f"<<red>> studies_urls_to_files_dir set to {studies_urls_to_files_dir}")


def dump_studies_urls_to_files(tab):
    # tab[study][f"File:{file_name}"] = {"url": image_url, "id": image_id}

    for study, files in tab.items():
        file = studies_urls_to_files_dir / f"{study}.json"
        with open(file, "w", encoding="utf-8") as f:
            json.dump(files, f, ensure_ascii=False, indent=2)
            print(f"Completed dumping {len(files)} items from {study} to {file}.")

    print(f"dump_studies_urls_to_files {len(tab)}")
