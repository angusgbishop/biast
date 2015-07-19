from kivy.factory import Factory

def create_error_popup(errorText):
    errorPopup = Factory.ErrorPopup(pos_hint={'center_x': 0.5,'center_y': 0.5})
    errorPopup.open()
    errorPopup.errorText = errorText