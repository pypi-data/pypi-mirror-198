from ._CharsStreamType import _CharsStreamType

class TextStreamType(_CharsStreamType):
    def __init__(self):
        super().__init__(extensions={'.log': 'Log', '.txt': 'Text'})
    def get_default_data(self):
        return list()
    def read(self, string):
        return type(self).read_lines(file=string)
    def write(self, string, data):
        type(self).write_lines(file=string, lines=data)
    def read_lines(file):
        lines = list()
        with open(file, 'r') as s:
            for line in s:
                assert line.endswith('\n')
                lines.append(line[:-1])
        return lines
    def write_lines(file, lines):
        with open(file, 'w') as s:
            for line in lines:
                print(line, file=s)
 
