from .coolapk_token import request

main_page_url = "https://api.coolapk.com/v6/main/indexV8?page=1&firstLaunch=0&installTime=0"

def is_post(n):
    if "id" in n:
        return True
    else:
        return False

def main_page(firstItem: int = 0):
    if firstItem == 0:
        __n = request("{0}".format(main_page_url))
    else:
        __n = request("{0}&{1}".format(main_page_url,firstItem))

    n = list(filter(is_post, __n))
    return n
