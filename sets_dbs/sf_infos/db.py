"""
python3 core8/pwb.py sets_dbs/sf_infos/db 54575469

from sets_dbs.sf_infos.db import insert_url_file # insert_url_file(url, file)

"""
import sys
from pathlib import Path
from fix_mass.sqlite_bot import SqlLiteFilesDB

Dir = Path(__file__).parent
db_path = Dir / "sf_infos.sqlite"
main_db_bot = SqlLiteFilesDB(db_path)


def insert_infos(data):
    """Insert information into the database."""
    try:
        return main_db_bot.insert_infos(data)
    except Exception as e:
        print(f"Failed to insert data: {e}")
        return None


def insert_url_file(url, file):
    return main_db_bot.insert_url_file(url, file)


def insert_all_infos(data_list_or, prnt=True):
    return main_db_bot.insert_all_infos(data_list_or, prnt=prnt)


def insert(data):
    return main_db_bot.insert(data)


def find_data(url="", urlid="", file=""):
    return main_db_bot.find_data(url=url, urlid=urlid, file=file)


def update_data(url="", urlid="", file=""):
    return main_db_bot.update_data(url=url, urlid=urlid, file=file)


def query(sql):
    return main_db_bot.query(sql)


def find_from_data_db(url, urlid):
    return main_db_bot.find_from_data_db(url, urlid)


def test():
    # Insert sample data
    insert(
        {
            "url": "https://prod-images-static.radiopaedia.org/images/33333333/xxxxxxxxxxx.JPG",
            "urlid": "",
            "file": "",
        }
    )
    insert(
        {
            "url": "",
            "urlid": "",
            "file": "File:tests.jpg",
        }
    )

    # Retrieve data
    data = main_db_bot.get_data("infos")
    data = list(data)
    # for row in data: print(row)
    print(f"len data in table (infos): {len(data)}")


def test2():
    print("________")
    # Retrieve data
    # data = main_db_bot.get_data("infos")
    # for row in data: print(row)
    # ---
    ids = [arg.strip() for arg in sys.argv if arg.isdigit()]
    # ---
    ids.extend([""])
    # ---
    print(f"ids: {ids}")
    # ---
    for x in ids:
        data = main_db_bot.select({"urlid": x}, "infos")
        # ---
        print(data)
    # ---
    # print(main_db_bot.select({"url": ""}, "infos"))


def test3():
    qua = "SELECT * from infos"
    # ---
    print(qua)
    # ---
    result = query(qua)
    # ---
    print(f"len result: {len(result)}")
    # ---
    if "printall" in sys.argv:
        for row in result:
            print(row)


if __name__ == "__main__":
    if "test" in sys.argv:
        test()
    elif "test3" in sys.argv:
        test3()
    else:
        test2()
