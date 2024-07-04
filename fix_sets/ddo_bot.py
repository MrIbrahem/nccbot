"""
from fix_sets.ddo_bot import ddo
"""
import sys
from time import sleep
from newapi import printe
from fix_sets.lists.studies_fixed import studies_fixed_done
from fix_sets.bots.has_url import already_has_url


def make_tabs(ids):
    length = (len(ids) // 10) + 1
    length = 1500
    # ---
    tabs = {}
    for i in range(0, len(ids), length):
        num = i // length + 1
        # ---
        tabs[str(num)] = ids[i : i + length]
        # ---
        command = f'tfj run fix{num} --mem 1Gi --image python3.9 --command "'
        command += f"$HOME/local/bin/python3 core8/pwb.py fix_sets/new_all get:{num} {len(tabs[str(num)])}"
        command += '"'
        # ---
        printe.output(command)
    # ---
    return tabs


def ddo(taba, spli=True):
    ids = taba
    # ---
    printe.output("<<green>> ----------------\nstart ddo:")
    # ---
    printe.output(f"Ids: <<yellow>>{len(ids):,},")
    # ---
    if "nodone" not in sys.argv:
        Done = studies_fixed_done
        # ---
        printe.output("\tworking after_done:, add 'nodone' to skip this..")
        # after_done = [x for x in ids if x not in Done]
        after_done = set(ids) - set(Done)
        after_done = list(after_done)
        # ---
        printe.output(f"\t\t ids after_done: <<yellow>>{len(after_done):,}")
        # ---
        ids = after_done
    # ---
    if "hasskip" not in sys.argv:
        printe.output(f"\n\t already_has_url: <<yellow>>{len(already_has_url):,}")
        # ---
        printe.output("\t\tworking after_has_urls:, add 'hasskip' to skip this..")
        # after_has_urls = [x for x in ids if x not in already_has_url]
        after_has_urls = set(ids) - set(already_has_url)
        after_has_urls = list(after_has_urls)
        # ---
        # printe.output(f"all ids: {len(ids)}, already_has_url:{len(already_has_url)}, after_has_urls: {len(after_has_urls)}")
        # ---
        printe.output(f"\t\t ids after_has_urls: <<yellow>>{len(after_has_urls):,}")
        # ---
        ids = after_has_urls
    # ---
    printe.output("<<yellow>> ----------------")
    if spli:
        tabs = make_tabs(ids)
        # ---
        for arg in sys.argv:
            arg, _, value = arg.partition(":")
            if arg == "get":
                ids = tabs[value]
                printe.output(f"work in {len(ids)} ids")
        del tabs
    # ---
    printe.output("<<green>> \n end ddo\n----------------")
    # ---
    sleep(2)
    # ---
    return ids
