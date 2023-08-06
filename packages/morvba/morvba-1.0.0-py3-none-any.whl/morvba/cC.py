import configparser
import os
from typing import Optional

class C:
    def __init__(self):
        pass

    def savesetting(self, a: str = '', b: str = '', c: str = '', d: str = '') -> None:
        try:
            path = "settings"
            if not os.path.exists(path):
                os.makedirs(path)
            config = configparser.ConfigParser()
            config[a + '_' + b + '_' + c] = {'key': d}
            with open(os.path.join(path, a + '_' + b + '_' + c + '.ini'), 'w') as configfile:
                config.write(configfile)
        except Exception as e:
            #print(f"Error in savesetting: {e}")
            pass

    def getsetting(self, a: str = '', b: str = '', c: str = '', d: str = '') -> Optional[str]:
        try:
            path = "settings"
            if not os.path.exists(path):
                os.makedirs(path)
            config = configparser.ConfigParser()
            config.read(os.path.join(path, a + '_' + b + '_' + c + '.ini'))
            if d == '':
                return config.get(a + '_' + b + '_' + c, 'key')
            else:
                self.savesetting(a, b, c, d)
                return d
        except Exception as e:
            #print(f"Error in getsetting: {e}")
            return ''

    def left(self, str_text: str = '', int_len: int = 1) -> str:
        return str_text[:int_len]

    def right(self, str_text: str = '', int_len: int = 1) -> str:
        return str_text[-int_len:]

    def mid(self, str_text: str = '', int_start: int = 1, int_len: int = 1) -> str:
        return str_text[int_start - 1:(int_start + int_len - 1)]

    def pricap(self, str_text: str = '') -> str:
        return str_text.title()

    def instr(self, int_start: int = 1, str_text: str = '', str_what: str = '') -> int:
        return str_text.find(str_what, int_start - 1) + 1

    def trim(self, str_text: str = '', str_char: str = ' ') -> str:
        x = str_text.strip()
        while self.instr(1, x, '  ') > 0:
            x = x.replace('  ', ' ')
        return x

    def pkey(self, str_text: str = '', str_ini: str = '', str_end: str = '', boo_trim: bool = True) -> str:
        if self.instr(1, str_text, str_ini) > 0 and self.instr(1, str_text, str_end) > 0:
            if boo_trim:
                return self.trim(self.mid(str_text, self.instr(1, str_text, str_ini) + len(str_ini),
                                          self.instr(self.instr(1, str_text, str_ini) + len(str_ini), str_text,
                                                     str_end) - (self.instr(1, str_text, str_ini) + len(str_ini))))
            else:
                return self.mid(str_text, self.instr(1, str_text, str_ini) + len(str_ini),
                                self.instr(self.instr(1, str_text, str_ini) + len(str_ini), str_text, str_end) - (
                                            self.instr(1, str_text, str_ini) + len(str_ini)))
        else:
            return ''

# Wrapper functions
def savesetting(a: str = '', b: str = '', c: str = '', d: str = '') -> None:
    c_instance = C()
    return c_instance.savesetting(a, b, c, d)


def getsetting(a: str = '', b: str = '', c: str = '', d: str = '') -> Optional[str]:
    c_instance = C()
    return c_instance.getsetting(a, b, c, d)


def left(str_text: str = '', int_len: int = 1) -> str:
    c_instance = C()
    return c_instance.left(str_text, int_len)


def right(str_text: str = '', int_len: int = 1) -> str:
    c_instance = C()
    return c_instance.right(str_text, int_len)


def mid(str_text: str = '', int_start: int = 1, int_len: int = 1) -> str:
    c_instance = C()
    return c_instance.mid(str_text, int_start, int_len)


def pricap(str_text: str = '') -> str:
    c_instance = C()
    return c_instance.pricap(str_text)


def instr(int_start: int = 1, str_text: str = '', str_what: str = '') -> int:
    c_instance = C()
    return c_instance.instr(int_start, str_text, str_what)


def trim(str_text: str = '', str_char: str = ' ') -> str:
    c_instance = C()
    return c_instance.trim(str_text, str_char)


def pkey(str_text: str = '', str_ini: str = '', str_end: str = '', boo_trim: bool = True) -> str:
    c_instance = C()
    return c_instance.pkey(str_text, str_ini, str_end, boo_trim)
