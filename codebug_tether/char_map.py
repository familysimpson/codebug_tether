"""4x5 character map.
https://github.com/tompreston/4x5-Font
http://clubweb.interbaun.com/~rc/Papers/microfont.pdf
"""
char_map = {
    '': [0x0, 0x0, 0x0, 0x0, 0x0],
    ' ': [0x0, 0x0, 0x0, 0x0, 0x0],
    '!': [0x4, 0x4, 0x4, 0x0, 0x4],
    '#': [0x6, 0xf, 0x6, 0xf, 0x6],
    '\'': [0x0, 0xa, 0x0, 0x0, 0x0],
    '%': [0x7, 0xe, 0x4, 0x7, 0xe],
    '$': [0x7, 0xa, 0x6, 0x5, 0xe],
    '"': [0x1, 0x2, 0x0, 0x0, 0x0],
    '&': [0x2, 0x5, 0x6, 0xa, 0x5],
    ')': [0x4, 0x2, 0x2, 0x2, 0x4],
    '(': [0x4, 0x8, 0x8, 0x8, 0x4],
    '+': [0x0, 0x2, 0x7, 0x2, 0x0],
    '*': [0x0, 0x6, 0xf, 0x6, 0x0],
    '-': [0x0, 0x0, 0x0, 0xf, 0x0],
    ',': [0x0, 0x0, 0x0, 0x2, 0x4],
    '/': [0x1, 0x1, 0x2, 0x4, 0x8],
    '.': [0x0, 0x0, 0x0, 0x0, 0x4],
    '1': [0x2, 0x6, 0x2, 0x2, 0x2],
    '0': [0x6, 0xb, 0xf, 0xd, 0x6],
    '3': [0xe, 0x1, 0x6, 0x1, 0xe],
    '2': [0xe, 0x1, 0x6, 0x8, 0xf],
    '5': [0xf, 0x8, 0xe, 0x1, 0xe],
    '4': [0x2, 0x6, 0xa, 0xf, 0x2],
    '7': [0xf, 0x1, 0x2, 0x4, 0x8],
    '6': [0x6, 0x8, 0xe, 0x9, 0x6],
    '8': [0x6, 0x9, 0x6, 0x9, 0x6],
    '9': [0x6, 0x9, 0xf, 0x1, 0x6],
    ':': [0x0, 0x4, 0x0, 0x4, 0x0],
    ';': [0x0, 0x4, 0x0, 0x4, 0x8],
    '<': [0x2, 0x4, 0x8, 0x4, 0x2],
    '=': [0x0, 0xf, 0x0, 0xf, 0x0],
    '>': [0x4, 0x2, 0x1, 0x2, 0x4],
    '?': [0x6, 0x9, 0x2, 0x0, 0x2],
    '@': [0x6, 0xd, 0xb, 0x8, 0x6],
    'A': [0x4, 0xa, 0xe, 0xa, 0xa],
    'B': [0xe, 0x9, 0xe, 0x9, 0xe],
    'C': [0x6, 0x9, 0x8, 0x9, 0x6],
    'D': [0xe, 0x9, 0x9, 0x9, 0xe],
    'E': [0xf, 0x8, 0xe, 0x8, 0xf],
    'F': [0xf, 0x8, 0xe, 0x8, 0x8],
    'G': [0x6, 0x8, 0xb, 0x9, 0x6],
    'H': [0x9, 0x9, 0xf, 0x9, 0x9],
    'I': [0xe, 0x4, 0x4, 0x4, 0xe],
    'J': [0x1, 0x1, 0x1, 0x9, 0x6],
    'K': [0x9, 0xa, 0xc, 0xa, 0x9],
    'L': [0x8, 0x8, 0x8, 0x8, 0xf],
    'M': [0x9, 0xf, 0xf, 0x9, 0x9],
    'N': [0x9, 0xd, 0xf, 0xb, 0x9],
    'O': [0x6, 0x9, 0x9, 0x9, 0x6],
    'P': [0xe, 0x9, 0xe, 0x8, 0x8],
    'Q': [0x6, 0x9, 0x9, 0xb, 0x7],
    'R': [0xe, 0x9, 0xe, 0xa, 0x9],
    'S': [0x7, 0x8, 0x6, 0x1, 0xe],
    'T': [0xe, 0x4, 0x4, 0x4, 0x4],
    'U': [0x9, 0x9, 0x9, 0x9, 0x6],
    'V': [0x9, 0x9, 0x9, 0x6, 0x6],
    'W': [0x9, 0x9, 0xf, 0xf, 0x9],
    'X': [0x9, 0x9, 0x6, 0x9, 0x9],
    'Y': [0x9, 0x5, 0x2, 0x2, 0x2],
    'Z': [0xf, 0x2, 0x4, 0x8, 0xf],
    '[': [0xe, 0x8, 0x8, 0x8, 0xe],
    '\\': [0x8, 0x8, 0x4, 0x2, 0x1],
    ']': [0x7, 0x1, 0x1, 0x1, 0x7],
    '^': [0x4, 0xa, 0x0, 0x0, 0x0],
    '_': [0x0, 0x0, 0x0, 0x0, 0xf],
    '`': [0x4, 0x2, 0x0, 0x0, 0x0],
    'a': [0x0, 0x5, 0xb, 0xb, 0x5],
    'b': [0x8, 0x8, 0xe, 0x9, 0xe],
    'c': [0x0, 0x7, 0x8, 0x8, 0x7],
    'd': [0x1, 0x1, 0x7, 0x9, 0x7],
    'e': [0x0, 0x6, 0xf, 0x8, 0x7],
    'f': [0x3, 0x4, 0xe, 0x4, 0x4],
    'g': [0x7, 0x9, 0x7, 0x1, 0x7],
    'h': [0x8, 0x8, 0xe, 0x9, 0x9],
    'i': [0x0, 0x2, 0x0, 0x2, 0x2],
    'j': [0x1, 0x0, 0x1, 0x1, 0x6],
    'k': [0x8, 0xa, 0xc, 0xa, 0x9],
    'l': [0xc, 0x4, 0x4, 0x4, 0xe],
    'm': [0x0, 0x9, 0xf, 0xf, 0x9],
    'n': [0x0, 0xe, 0x9, 0x9, 0x9],
    'o': [0x0, 0x6, 0x9, 0x9, 0x6],
    'p': [0x0, 0xe, 0x9, 0xe, 0x8],
    'q': [0x0, 0x6, 0x9, 0x7, 0x1],
    'r': [0x0, 0xb, 0xc, 0x8, 0x8],
    's': [0x0, 0x7, 0x4, 0x2, 0xe],
    't': [0x4, 0xe, 0x4, 0x4, 0x3],
    'u': [0x0, 0x9, 0x9, 0x9, 0x6],
    'v': [0x0, 0x9, 0x9, 0x6, 0x6],
    'w': [0x0, 0x9, 0xf, 0xf, 0x6],
    'x': [0x0, 0x9, 0x6, 0x6, 0x9],
    'y': [0x0, 0x9, 0x7, 0x1, 0x6],
    'z': [0x0, 0xf, 0x2, 0x4, 0xf],
    '{': [0x6, 0x4, 0xc, 0x4, 0x6],
    '|': [0x4, 0x4, 0x0, 0x4, 0x4],
    '}': [0xc, 0x4, 0x6, 0x4, 0xc],
    '~': [0x0, 0x0, 0x5, 0xa, 0x0],
    'unknown': [0xf, 0x9, 0x9, 0x9, 0xf],
}


class CharSprite(object):
    """A character sprite."""

    width = 4
    height = 5

    def __init__(self, char):
        self.char = char
        if char not in char_map:
            char = 'unknown'
        self.pixel_state = [[(char_map[char][row] >> shift) & 0x1
                           for shift in reversed(range(4))]
                          for row in range(5)]


class StringSprite(object):
    """A sprite storing a string."""

    def __init__(self, string, direction='right'):
        self.string = string

        if "r" in direction.lower() or "l" in direction.lower():
            self.width = 5 * len(string)
            self.height = 5
        elif "u" in direction.lower() or "d" in direction.lower():
            self.width = 4
            self.height = 6 * len(string)

        self.led_state = [[0 for i in range(self.width)]
                          for j in range(self.height)]

        for char_index, c in enumerate(self.string):
            char_sprite = CharSprite(c)
            for y in range(char_sprite.height):
                for x in range(char_sprite.width):

                    if "r" in direction.lower():
                        self.led_state[y][x+(char_index*5)] = \
                            char_sprite.led_state[y][x]

                    if "l" in direction.lower():
                        self.led_state[y][x+(self.width-(char_index+1)*5)] = \
                            char_sprite.led_state[y][x]

                    if "d" in direction.lower():
                        self.led_state[y+(char_index*6)][x] = \
                            char_sprite.led_state[y][x]

                    if "u" in direction.lower():
                        self.led_state[y+(self.height-(char_index+1)*6)][x] = \
                            char_sprite.led_state[y][x]
