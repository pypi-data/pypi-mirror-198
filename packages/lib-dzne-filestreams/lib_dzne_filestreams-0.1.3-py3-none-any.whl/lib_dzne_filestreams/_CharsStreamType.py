import tempfile
from ._StreamType import _StreamType as StreamType

class _CharsStreamType(StreamType):
    def data_to_str(self, data):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpfile = os.path.join(tmpdir, 'a')
            self.write(tmpfile, data)
            with open(tmpfile, 'r') as s:
                return s.read() 
