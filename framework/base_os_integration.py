import pyautogui as pag


class BaseOsIntegration:
    @staticmethod
    def type_write(text):
        pag.typewrite(text)

    @staticmethod
    def press_kw_button(button_name):
        if button_name not in pag.KEY_NAMES:
            raise NameError
        pag.press(button_name)
