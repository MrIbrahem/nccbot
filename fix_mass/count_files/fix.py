"""

python3 core8/pwb.py mass/radio/st3sort/count_files/fix 134732

"""
import json
import os
import sys
import requests

from newapi import printe
from ncc_jsons.dir_studies_bot import studies_urls_to_files_dirs


def get_stcks(study_id):
    new_url = f"https://radiopaedia.org/studies/{study_id}/stacks"
    print(f"get_images_stacks: study_id: {study_id}, new_url: {new_url}")
    # ---
    try:
        response = requests.get(new_url, timeout=10)
    except Exception as e:
        print(f"Failed to retrieve content from the URL. Error: {e}")
        return {}
    # ---
    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print(f"Failed to retrieve content from the URL. Status Code: {response.status_code}")
        return {}

    text = response.text
    if not text.startswith("[") and not text.endswith("]"):
        print(f"Failed to retrieve content from the URL. Status Code: {response.status_code}")
        return {}

    json_data = json.loads(text)

    return json_data


def make_text(modality, files, set_title):
    # ---
    text = f"== {modality} ==\n"

    text += "{{Imagestack\n|width=850\n"
    text += f"|title={set_title}\n|align=centre\n|loop=no\n"
    # ---
    # sort files
    files = {k: v for k, v in sorted(files.items())}
    # ---
    for n, image_name in files.items():
        text += f"|{image_name}|\n"
    # ---
    text += "\n}}\n\n"
    # ---
    return text


def one_study(json_data, url_to_file, study_id):
    # ---
    text = ""
    # ---
    for x in json_data:
        # ---
        noo = 0
        # ---
        print(x.keys())
        # ---
        modality = x["modality"]
        images = x["images"]
        # ---
        files = {}
        # ---
        # sort images by position key
        images = sorted(images, key=lambda x: x["position"])
        # ---
        for n, image in enumerate(images, start=1):
            # ---
            public_filename = image["public_filename"]
            # ---
            file_name = url_to_file.get(public_filename)
            # ---
            if not file_name:
                noo += 1
                file_name = public_filename
            # ---
            files[n] = file_name
            # ---
        # ---
        print(f"noo: {noo}")
        print(f"files: {len(files)}")
        # ---
        text += make_text(modality, files, study_id)
        # ---
    # ---
    print(text)


def main(ids):
    # ---
    for study_id in ids:
        # ---
        json_file = studies_urls_to_files_dir / f"{study_id}.json"
        # ---
        if not os.path.exists(json_file):
            printe.output(f"<<red>> {json_file} not found")
            continue
        # ---
        with open(json_file, encoding="utf-8") as f:
            data = json.load(f)
        # ---
        url_to_file = {v["url"]: x for x, v in data.items()}
        # ---
        json_data = get_stcks(study_id)
        # ---
        if not json_data:
            printe.output(f"<<red>> {json_file} not found")
            continue
        # ---
        one_study(json_data, url_to_file, study_id)
        # ---


if __name__ == "__main__":
    ids = [arg for arg in sys.argv[1:] if arg.isdigit()]
    main(ids)
