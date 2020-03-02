# This is a class of buttons with values and a "is_on" boolean


class Button:
    def __init__(self, value, is_on=True):
        self.value = value
        self.is_on = is_on

    def render(self, width, is_on):
        if is_on:
            return f'<button id="{self.value}" name="{self.value}" ' \
                   f'value="{self.value}" style="width:{width}%">{self.value}</button>\n'
        else:
            return f'<button id="{self.value}" name="{self.value}" ' \
                   f'value="{self.value}" style="width:{width}%; background-color:red">{self.value}</button>\n'

    def turn_off(self):
        self.is_on = False

    def check_guess(self, correct_value, button_list):
        if self.value == correct_value:
            return True
        elif self.value < correct_value:
            button_index = 0
            while button_index <= self.value:
                button_list[button_index].turn_off()
                button_index += 1
        else:
            button_index = len(button_list) - 1
            while button_index >= self.value:
                button_list[button_index].turn_off()
                button_index -= 1
        return False
