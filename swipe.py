from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_MOUSE, POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton


def swipe_object1_to_object2_by_id(object1_id, object2_id):
    """Swipes Object 1 to coordinates of object 2

      Parameters:
      object1_id (str): accesibility id of object 1
      object2_id (str): accesibility id of object 2

     """

    object1_id = appium_driver.find_element(
        MobileBy.ACCESSIBILITY_ID, object1_id)
    object1_id_x = object1_id.x
    object1_id_y = object1_id.y
    object2_id = appium_driver.find_element(
        MobileBy.ACCESSIBILITY_ID, object1_id)
    object2_id_x = object2_id.x
    object2_id_y = object2_id.y
    swipe = ActionBuilder(appium_driver)
    finger = swipe.add_pointer_input(POINTER_TOUCH, "finger")
    finger.create_pointer_move(duration=0, x=object1_id_x, y=object1_id_y)
    finger.create_pointer_down(MouseButton.LEFT)
    finger.create_pointer_move(
        duration=500, x=object2_id_x, y=object2_id_y)
    finger.create_pointer_up(MouseButton.LEFT)
    swipe.perform()
