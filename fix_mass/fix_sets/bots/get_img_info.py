"""

python3 core8/pwb.py fix_mass/fix_sets/bots/get_img_info

from fix_mass.fix_sets.bots.get_img_info import one_img_info

"""
import sys
import re
import json

# import os
from newapi import printe
from newapi.ncc_page import NEW_API
from fix_mass.fix_sets.jsons_dirs import get_study_dir  # , jsons_dir
from fix_mass.helps_bot.file_bot import from_cach, dumpit

api_new = NEW_API("www", family="nccommons")
api_new.Login_to_wiki()

# st_dic_infos = jsons_dir / "studies_files_infos"


def dump_st(data, study_id):
    # ---
    study_id_dir = get_study_dir(study_id)
    # ---
    file = study_id_dir / "img_info.json"
    # ---
    dumpit(data, file)

def get_cach_img_info(study_id):
    # ---
    study_id_dir = get_study_dir(study_id)
    # ---
    file = study_id_dir / "img_info.json"
    # ---
    return from_cach(file)


def gt_img_info(titles, id_to_url=None):
    # ---
    if not id_to_url:
        id_to_url = {}
    # ---
    titles = [titles] if not isinstance(titles, list) else titles
    # ---
    titles = [x for x in titles if x]
    # ---
    info = {}
    printe.output(f"one_img_info: {len(titles)=}")
    # ---
    _x = {
        "pages": [
            {
                "pageid": 1382521,
                "ns": 6,
                "title": "File:Appendicitis (CT angiogram) (Radiopaedia 154713-134732 This comic explains the pathophysiology of appendicitis. 4).jpg",
                "extlinks": [
                    {"url": "https://radiopaedia.org/cases/appendicitis-ct-angiogram"},
                    {"url": "https://creativecommons.org/licenses/by-nc-sa/3.0/"},
                    {"url": "http://creativecommons.org/licenses/by-nc-sa/3.0/"},
                    {"url": "https://radiopaedia.org/cases/154713/studies/134732"},
                    {"url": "https://prod-images-static.radiopaedia.org/images/61855973/2bdea73556100c7fb71c76c05394c69df2b00153ab6b00647c53c51ee7c88f3d.jpg"},
                    {"url": "https://radiopaedia.org/users/stefan-tigges?lang=us"},
                ],
            }
        ]
    }
    # ---
    params = {
        "action": "query",
        # "titles": "|".join(titles),
        # "prop": "revisions|categories|info|extlinks",
        "prop": "revisions|extlinks",
        # "clprop": "sortkey|hidden", # categories
        "rvprop": "content",  # revisions
        # "cllimit": "max",  # categories
        "ellimit": "max",  # extlinks
        "formatversion": "2",
    }
    # ---
    # work with 40 titles at once
    for i in range(0, len(titles), 40):
        group = titles[i : i + 40]
        params["titles"] = "|".join(group)
        # ---
        # print("|".join(group))
        # ---
        data = api_new.post_params(params)
        # ---
        error = data.get("error", {})
        if error:
            printe.output(json.dumps(error, indent=2))
        # ---
        pages = data.get("query", {}).get("pages", [])
        # ---
        for page in pages:
            extlinks = page.get("extlinks", [])
            title = page.get("title")
            # ---
            # info[title] = {"img_url": "", "case_url": "", "study_url": "", "caseId": "", "studyId": "", "img_id": ""}
            info[title] = {"img_url": "", "img_id": ""}
            # ---
            for extlink in extlinks:
                url = extlink.get("url")
                # ma = re.match("https://radiopaedia.org/cases/(\d+)/studies/(\d+)", url)
                if url.find("/images/") != -1:
                    info[title]["img_url"] = url

                # elif re.match(r"^https://radiopaedia.org/cases/[^\d\/]+$", url):
                #     info[title]["case_url"] = url

                # elif ma:
                #     info[title]["study_url"] = url
                #     info[title]["caseId"] = ma.group(1)
                #     info[title]["studyId"] = ma.group(2)
            # ---
            revisions = page.get("revisions")
            if info[title]["img_url"]:
                continue
            # ---
            if not revisions:
                continue
            # ---
            revisions = revisions[0]["content"]
            # match * Image ID: 58331091 in revisions.split("\n")
            ma = re.search(r"Image ID: (\d+)", revisions, re.IGNORECASE)
            if ma:
                info[title]["img_id"] = ma.group(1)
                info[title]["img_url"] = id_to_url.get(str(ma.group(1)), "")
            else:
                print(revisions)
    # ---
    # printe.output(json.dumps(pages, indent=2))
    # ---
    return info


def one_img_info(title, study_id, json_data):
    # ---
    if "oo" not in sys.argv:
        return {}
    # ---
    cach = get_cach_img_info(study_id)
    if cach:
        return cach
    # ---
    id_to_url = {}
    # ---
    for x in json_data:
        for image in x["images"]:
            id_to_url[str(image["id"])] = image["public_filename"]
    # ---
    info = gt_img_info(title, id_to_url)
    # ---
    dump_st(info, study_id)
    # ---
    return info


def test():
    title = [
        "File:1st metatarsal head fracture (Radiopaedia 99187-120594 Frontal 1).png",
        "File:Appendicitis (CT angiogram) (Radiopaedia 154713-134732 This comic explains the pathophysiology of appendicitis. 02).jpg",
    ]
    info = gt_img_info(title)
    # ---
    print(json.dumps(info, indent=2))


if __name__ == "__main__":
    test()
