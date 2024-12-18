"""
    ANSI

This file contain ANSI texts.
"""


""" ANSI keys definition """
KEY = "\033["

""" return ansi texture key """
def texture(key: int) -> str: return f"{KEY}{key}m"


class ANSI:
    """ ANSI definitions """

    """ Texture """
    class Texture:
        """ Texture definitions """

        """ Clear """
        CLEAR = texture(0)

        """ Font """
        class Font:
            """ Font definitions """
            BOLD = texture(1)
            THIN = texture(2)
            ITALIC = texture(3)
            UNDER_BAR = texture(4)
            BLINK = texture(5)
            FIRST_BLINK = texture(6)
            INVERT = texture(7)
            HIDE = texture(8)
            DelTHIN = texture(22)
            DelITALIC = texture(23)
            DelUNDER_BAR = texture(24)
            DelBLINK = texture(25)
            DelFIRST_BLINK = texture(26)
            DelINVERT = texture(27)
            DelHIDE = texture(28)
            ...

        """ Font color definitions """
        class FontColor:
            """ Font color definitions """
            BLACK = texture(30)
            RED = texture(31)
            GREEN = texture(32)
            YELLOW = texture(33)
            BLUE = texture(34)
            MAGENTA = texture(35)
            CYAN = texture(36)
            GRAY = texture(37)
            WHITE = texture(39)
            Clear = texture(39)
            ...

        """ Background color definitions """
        class BackgroundColor:
            """ Background color definitions """
            BLACK = texture(40)
            RED = texture(41)
            GREEN = texture(42)
            YELLOW = texture(43)
            BLUE = texture(44)
            MAGENTA = texture(45)
            CYAN = texture(46)
            GRAY = texture(47)
            ...

        ...

    ...


Tex = ANSI.Texture
F = Tex.Font
FC = Tex.FontColor
BC = Tex.BackgroundColor
