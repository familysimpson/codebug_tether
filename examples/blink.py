# only needed for testing
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

from codebug_tether import CodeBug
import time


if __name__ == '__main__':
    cb = CodeBug()
    for i in range(10):
        cb.set_row(0, 0b10101)
        cb.set_row(1, 0b01010)
        cb.set_row(2, 0b10101)
        cb.set_row(3, 0b01010)
        cb.set_row(4, 0b10101)
        time.sleep(1)
        cb.set_row(0, 0b01010)
        cb.set_row(1, 0b10101)
        cb.set_row(2, 0b01010)
        cb.set_row(3, 0b10101)
        cb.set_row(4, 0b01010)
        time.sleep(1)