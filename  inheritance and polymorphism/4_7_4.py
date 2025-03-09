class Note:
    __slots__ = ('_name', '_ton')

    def __init__(self, name: str, ton: int):
        self._validate_name(name)
        self._validate_ton(ton)
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_ton':
            self._validate_ton(value)
        elif key == '_name':
            self._validate_name(value)
        super().__setattr__(key, value)

    @staticmethod
    def _validate_name(name: str):
        if name not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
            raise ValueError('недопустимое значение аргумента')

    @staticmethod
    def _validate_ton(ton: int):
        if ton not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')


class Notes:
    __instance = None
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, '_do'):
            self._do = Note('до', 0)
            self._re = Note("ре", 0)
            self._mi = Note("ми", 0)
            self._fa = Note("фа", 0)
            self._solt = Note("соль", 0)
            self._la = Note("ля", 0)
            self._si = Note("си", 0)

    def __getitem__(self, item):
        if not isinstance(item, int) or not (0 <= item <= 6):
            raise IndexError('недопустимый индекс')

        return getattr(self, self.__slots__[item])


notes = Notes()