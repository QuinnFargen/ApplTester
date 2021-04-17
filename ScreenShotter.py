
def TakeScreenShot(driver, SSName):
    required_width = driver.execute_script(
        'return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script(
        'return document.body.parentNode.scrollHeight')
    driver.set_window_size(required_width, required_height)
    PicName = SSName + '.png'
    driver.find_element_by_tag_name(
        'body').screenshot(PicName)  # avoids scrollbar
