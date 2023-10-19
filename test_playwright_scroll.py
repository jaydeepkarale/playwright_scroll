from playwright.sync_api import expect, Keyboard, Page
import time
import random


def test_scroll_into_view_if_needed(page: Page):
    """
    Test verifies if the contact us section is visible and scrolls to it
    """        
    page.goto('https://www.lambdatest.com/selenium-playground/')
    base_locator = page.get_by_role('link', name="Contact Us")
    expect(base_locator).to_be_visible()
    page.pause()
    base_locator.scroll_into_view_if_needed()
    page.pause()        
    page.close()

def test_scroll_into_view_if_needed_element_already_in_viewport(page: Page):
    """
    Test verifies if the Context Menu section is visible and no scroll happens
    """        
    age.goto('https://www.lambdatest.com/selenium-playground/')
    ase_locator = page.get_by_role('link', name=" Context Menu")
    xpect(base_locator).to_be_visible()
    age.pause()
    ase_locator.scroll_into_view_if_needed()
    age.pause()        
    age.close()


def test_scroll_using_mouse_wheel(page: Page):  
    page.set_viewport_size(
        {
            "width": 1920,
            "height": 1080
        }
    ) 
    page.goto("https://ecommerce-playground.lambdatest.io/")
    page.get_by_role("button", name="Shop by Category").click()
    page.get_by_role("link", name="Software").click()
    page_to_be_scrolled = page.get_by_role("combobox", name="Show:").select_option("https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=17&limit=75")
    print(page_to_be_scrolled[0].split("=")[-1])
    page.goto(page_to_be_scrolled[0])    
    # Since image are lazy-loaded scroll to bottom of page
    # the range is dynamically decided based on the number of items i.e. we take the range from limit
    # https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=17&limit=75
    for i in range(int(page_to_be_scrolled[0].split("=")[-1])):
        page.mouse.wheel(0, 100)
        i += 1
        time.sleep(0.1)

def test_scroll_using_keyboard_press(page: Page):
    page.set_viewport_size(
        {
            "width": 1920,
            "height": 1080
        }
    ) 
    page.goto("https://playwright.dev/python/docs/api/class-keyboard")

    # delay is used to control time between keypress and key release    
    for _ in range(5):
        page.keyboard.press("PageDown", delay=1000)

    for _ in range(5):
        page.keyboard.press("PageUp", delay=1000)

    for _ in range(30):
        page.keyboard.press("ArrowDown", delay=100)
    
    for _ in range(30):
        page.keyboard.press("ArrowUp", delay=100)



def test_horizontal_scroll(page: Page):
    """
    Test verifies if the contact us section is visible and scrolls to it
    """
    page.set_viewport_size(
        {
            "width": 1920,
            "height": 1080
        }
    )     
    page.goto('https://codepen.io/ReGGae/full/QZxdVX/')
    for _ in range(50):
        base_locator = page.frame_locator("#result").locator(f"div:nth-child(3) > article:nth-child({random.choice([1,2,3,4,5])}) > .slide__inner > .slide__img")
        base_locator.scroll_into_view_if_needed()   
        time.sleep(0.5)         
    page.close()
    