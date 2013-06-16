import re


def main():
    """docstring for main"""
    s = "This is a test"
    fields = re.split("\s+", s)
    x = " ".join([i[::-1] for i in fields[::-1]])
    print x
    pass
if __name__ == '__main__':
    main()
