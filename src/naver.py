from selenium import webdriver


def get_paging_element(driver):

    main_content = driver.find_element_by_id("main_content")
    paging_element = main_content.find_element_by_css_selector("div.paging")
    return paging_element


def is_next(paging_element):
    """
    :param paging_element:
    :return: ret, exist(boolean)
    """
    ret = 0
    exist = False
    try:
        if "다음" in paging_element.text:
            exist = True
    except Exception as e:
        print(e)
        return ret, exist

    ret = 1

    return ret, exist

def get_pages(paging_element):
    """
    :param paging_element:
    :return: ret, pages(list)
    """
    ret = 0
    pages = []
    try:
        pages = paging_element.text.strip().split(" ")
    except Exception as e:
        print(e)

    if pages:
        ret = 1

    return ret, pages
def click_next(paging_element):
    """
    :param paging_element:
    :return: ret
    """
    ret = 0

    try:
        clickables = paging_element.find_elements_by_css_selector("a")
        next_link = clickables[-1]
        # link_text = next_link.text
        next_link.click()
        ret = 1
    except Exception as e:
        print(e)

    return ret