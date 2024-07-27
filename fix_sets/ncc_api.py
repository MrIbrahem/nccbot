"""

from fix_sets.ncc_api import ncc_MainPage
from fix_sets.ncc_api import CatDepth
from fix_sets.ncc_api import post_ncc_params

"""
from newapi.ncc_page import NEW_API
from newapi.ncc_page import CatDepth
from newapi.ncc_page import MainPage as ncc_MainPage

api_new = NEW_API("www", family="nccommons")


def post_ncc_params(params, **kwargs):
    # ---
    result = api_new.post_params(params, **kwargs)
    # ---
    return result
