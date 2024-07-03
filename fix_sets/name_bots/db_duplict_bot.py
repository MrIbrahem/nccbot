"""

from fix_sets.name_bots.db_duplict_bot import find_url_file_upload

"""
import re
import jsonlines
from pathlib import Path
import mimetypes

# from pathlib import Paths
from newapi.ncc_page import NEW_API
from newapi import printe

from fix_sets.jsons_dirs import jsons_dir

# from sets_dbs.dp_infos.db_duplict import get_all_key_url_urlid, insert_url_file  # ,find_from_data_db as find_from_db_dp # insert_url_file(url, file)

api_new = NEW_API("www", family="nccommons")
api_new.Login_to_wiki()

url_to_file_file = jsons_dir / "find_from_url.jsonl"

if not url_to_file_file.exists():
    url_to_file_file.write_text('{"url": "", "file_name": ""}')

data1x = jsonlines.open(url_to_file_file)
data_maain = {d["url"]: d["file_name"] for d in data1x}

# db_data = get_all_key_url_urlid()
db_data = {}


def get_new_ext(error_info, file_name):
    """
    استخراج الامتداد الصحيح من رسالة الخطأ باستخدام وحدة pathlib
    """

    # Extract MIME type from the error message using mimetypes
    mime_type = re.findall(r"MIME type of the file \((.*?)\)", error_info)
    if len(mime_type) > 0:
        mime_type = mime_type[0]

    if not mime_type:
        print("MIME type could not be extracted from the error message.")
        return file_name

    print(f"{mime_type=}")

    # Extract the correct extension from the MIME type
    correct_ext = mimetypes.guess_extension(mime_type)
    if not correct_ext and mime_type == "image/x-bmp":
        correct_ext = ".bmp"

    if not correct_ext:
        print("Could not determine the correct file extension for the MIME type.")
        return file_name

    # استبدال الامتداد في اسم الملف
    new_file_name = str(Path(file_name).with_suffix(correct_ext))

    print(f"{new_file_name=}")

    return new_file_name


def match_urlid(url):
    # ---
    url_id = ""
    # ---
    # find id from url like: https://prod-images-static.radiopaedia.org/images/(\d+)/.*?$
    mat = re.match(r"https://prod-images-static.radiopaedia.org/images/(\d+)/.*?$", url)
    if mat:
        url_id = mat.group(1)
    # ---
    return url_id


def append_data(url, file_name):
    data_maain[url] = file_name
    # ---
    # insert_url_file(url, file_name)
    # ---
    # with jsonlines.open(url_to_file_file, mode="a") as writer:
    #     writer.write({"url": url, "file_name": file_name})


def get_from_api(url, filename="", do_ext=True):
    # ---
    # extension = get_image_extension(image_url)
    # ---
    if not filename:
        extension = "jpg"
        # ---
        ext = url.split("/")[-1]
        if ext.find(".") != -1:
            extension = ext.split(".")[-1].lower()
        # ---
        files = {
            "jpg": "Wiki.jpg",
            "png": "Test.png",
        }
        # ---
        filename = f"Wiki.{extension}"
        # ---
        filename = files.get(extension, filename)
    # ---
    params = {"action": "upload", "format": "json", "filename": filename, "url": url, "stash": 1, "formatversion": "2"}
    # ---
    # { "upload": { "result": "Warning", "warnings": { "duplicate": [ "Angiodysplasia_-_cecal_active_bleed_(Radiopaedia_168775-136954_Coronal_91).jpeg" ] }, "filekey": "1b00hc5unqxw.olk8pi.13.", "sessionkey": "1b00hc5unqxw.olk8pi.13." } }
    # ---
    data = api_new.post_params(params)
    # ---
    result = data.get("upload", {}).get("result", "")  # Success
    duplicate = data.get("upload", {}).get("warnings", {}).get("duplicate", [])
    error = data.get("error", {})
    # ---
    du = ""
    # ---
    if duplicate:
        du = "File:" + duplicate[0]
        du = du.replace("_", " ")
        # ---
        printe.output(f"duplicate, find_url_file_upload: {du}")
    elif result == "Success":
        printe.output(f"Success, find_url_file_upload: {url}")
    elif error:
        error_code = error.get("code", "")
        error_info = error.get("info", "")
        # ---
        printe.output(f"<<lightred>> error when upload_by_url, error_code:{error_code}")
        # ---
        if error_code == "verification-error":
            if do_ext and "MIME type of the file" in error_info:
                new_file_name = ext.get_new_ext(error_info, "wiki.jpg")
                if new_file_name:
                    return get_from_api(url, filename=new_file_name, do_ext=False)
    else:
        print(data)
    # ---
    return du


def from_cach_or_db(url, url_id=""):
    # ---
    if url in data_maain:
        da = data_maain[url]
        if da.find("https") == -1:
            # printe.output(f"find_url_file_upload: {data_maain[url]}")
            return da
    # ---
    # file_name = find_from_db_dp(url, "")
    file_name = ""
    # ---
    file_name = db_data.get(url) or (db_data.get(url_id) if url_id else "")
    # ---
    # if file_name: printe.output(f"<<green>> find_from_data_db: {url} -> {file_name}")
    # ---
    return file_name


def find_url_file_upload(url, do_api=True):
    # ---
    url_id = match_urlid(url)
    # ---
    in_cach = from_cach_or_db(url, url_id)
    # ---
    if in_cach and in_cach.find("https") == -1:
        # printe.output(f"find_url_file_upload, from_cach_or_db: {in_cach}")
        return in_cach
    # ---
    na = ""
    # ---
    if do_api:
        na = get_from_api(url)
    # ---
    if na:
        append_data(url, na)
    # ---
    return na
