"""

python3 core8/pwb.py fix_sets/by_count/co

from fix_sets.by_count.co import from_files, count_files
"""
import json
import tqdm
from newapi import printe
from pathlib import Path

from fix_sets.jsons_dirs import st_ref_infos
from fix_sets.lists.studies_fixed import studies_fixed_done

Dir = Path(__file__).parent

files_file = Dir / "by_count.json"
# ---
if not files_file.exists():
    files_file.write_text("{}")
    data = {}
else:
    data = json.loads(files_file.read_text(encoding="utf-8"))


data_keys = list(data.keys())
data_keys.extend(studies_fixed_done)

data_keys = list(set(data_keys))


def count_files(x):
    file_js = st_ref_infos / x / "stacks.json"
    with open(file_js, "r", encoding="utf-8") as f:
        # Combine loading and processing into a single expression (generator comprehension)
        public_filenames = {item["public_filename"] for item in json.load(f) for item in item.get("images", [])}
        all_files = len(public_filenames)

    return all_files


def get_and_log(ids):
    ids = [x for x in ids if x not in data]

    newdata = {x: count_files(x) for x in ids}

    data.update(newdata)

    with open(files_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        printe.output(f"<<green>> write {len(data)} to {files_file=}")

    return data


def from_stacks_files():
    printe.output("from_stacks_files:")

    lala = []

    for subdir in tqdm.tqdm(st_ref_infos.iterdir(), total=80000):
        if not subdir.is_dir():
            continue

        study_id = subdir.name
        if study_id in data_keys:
            continue

        file_js = subdir / "stacks.json"

        if file_js.exists():
            lala.append(study_id)

    return lala


def from_files():
    printe.output("from_files:")

    lala = from_stacks_files()

    lal2 = []

    for study_id in tqdm.tqdm(lala):
        lal2.append(study_id)

        if len(lal2) == 5000:
            get_and_log(lal2)
            lal2 = []

    lisst_of_s = get_and_log(lal2)

    return lisst_of_s


if __name__ == "__main__":
    from_files()
