import lib_dzne_tsv as _tsv
import tempfile as _tmp
import os as _os
from ._CharsStreamType import _CharsStreamType

class TabStreamType(_CharsStreamType):
    def read(self, string, *, strip=False, **kwargs):
        data = _tsv.read_DataFrame(string, **kwargs)
        if strip:
            data = data.applymap(lambda x: x.strip())
        return data
    def write(self, string, data, *, strip=False):
        if strip:
            data = data.applymap(lambda x: x.strip())
        _tsv.write_DataFrame(string, data)
    def get_default_data(self):
        with _tmp.TemporaryDirectory() as tmp:
            if self.extensions is None:
                file = _os.path.join(tmp, "a")
            else:
                file = _os.path.join(tmp, "a" + self.extensions.keys()[0])
            with open(file, "w") as s:
                pass
            return self.read(file)



                