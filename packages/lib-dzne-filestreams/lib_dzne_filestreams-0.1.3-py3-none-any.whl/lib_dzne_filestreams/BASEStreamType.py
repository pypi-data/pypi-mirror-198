import lib_dzne_basetables as _bt
from .TabStreamType import TabStreamType as _TST


class BASEStreamType(_TST):
    def __init__(self, basetype=None):
        self._basetype = basetype
        if basetype is None:
            x = None
        elif basetype in {'a', 'd', 'm', 'y', 'c'}:
            x = {f".{basetype}base": f"{basetype}base"}
        else:
            raise ValueError()
        super().__init__(extensions=x)
    def get_default_data(self):
        return _bt.table.make(basetype=self._basetype)
    def read(self, string, **kwargs):
        data = super().read(string, **kwargs)
        data = _bt.table.make(data, basetype=self._basetype)
        return data
    def write(self, string, data):
        _bt.table.check(data, basetype=self._basetype)
        super().write(string, data)