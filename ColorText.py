# Copyright Kigipaul 2018.
'''
This class generates ANSI character codes to string colors.
'''


class ColorText():
    B = 30  # Black
    R = 31  # Red
    G = 32  # Green
    Y = 33  # Yellow
    L = 34  # Blue
    P = 35  # Pink
    C = 36  # Cyan
    W = 37  # White

    def __init__(self):
        '''
        Init Color Text
        '''
        self._INPUT = "BRGYLPCW"

    def get_back(self, char):
        '''Get background ANSI code

        Args:
            char: type=string, which in self._INPUT

        Returns:
            Background ANSI code
        '''
        rs = self.B + 10
        if char in self._INPUT:
            rs = getattr(self, char) + 10
        return rs

    def parse_style_str(self, style_str):
        '''Parse style string to ANSI code string

        Args:
            style_str: type=string, color string
                    Format: [bright]<front color>[background color]

        Returns:
            self.get_color(**)
        '''
        bright = False
        front = self.W
        back = self.get_back('B')
        style_str = style_str.upper()

        if len(style_str) > 0:
            str_list = list(style_str)
            if len(str_list) == 1:
                if str_list[0] in self._INPUT:
                    front = getattr(self, str_list[0])
            elif len(str_list) == 2:
                try:
                    bright = bool(int(str_list[0]))
                except:
                    bright = False
                if str_list[1] in self._INPUT:
                    front = getattr(self, str_list[1])
            elif len(str_list) > 2:
                try:
                    bright = bool(int(str_list[0]))
                except:
                    bright = False
                if str_list[1] in self._INPUT:
                    front = getattr(self, str_list[1])
                if str_list[2] in self._INPUT:
                    back = self.get_back(str_list[2])
        return self.get_color(
                front=front,
                back=back,
                bright=bright
                )

    def get_color(self, front, bright=False, back=0):
        '''Generate ANSI character code

        Args:
            front: type=int, which by globals attr
            bright: type=bool, True:bright, False brightness
            back: type=int, which by self.get_back(<color_str>)

        Returns:
            ANSI character color string
        '''
        rs = "m"
        if back != 0:
            rs = ";{}{}".format(back, rs)
        rs = "{}{}".format(front, rs)
        if bright:
            rs = "{};{}".format('1', rs)
        rs = "\033[{}".format(rs)
        return rs

    def text(self, msg, style='0W'):
        '''Generates ANSI character codes to text

        Args:
            msg: String text
            style: Color style string.
                   (Format: [bright]<front color>[background color])

        Returns:
            The string with ANSI character color codes

        Example:
            msg = "test"
            style = "1WR"
            returns a text with bright white words and red background
        '''
        color = self.parse_style_str(style)
        msg = "{}{}\033[0m".format(color, msg)
        return msg
