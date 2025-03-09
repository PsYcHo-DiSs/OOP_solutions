class FileAcceptor:
    def __init__(self, *exts):
        self._ext_lst = tuple(exts)

    def __add__(self, other):
        if isinstance(other, FileAcceptor):
            combined_exts = self._ext_lst + other._ext_lst
            return FileAcceptor(*combined_exts)

    def _is_valid(self, file):
        if isinstance(file, str) and '.' in file:
            file_ext = file.split(".")[-1]
            return file_ext in self._ext_lst
        return False

    def __call__(self, filename):

        return self._is_valid(filename)