class DigitRetrieve:
    def __call__(self, item, *args, **kwargs):
        try:
            return int(item)
        except ValueError:
            return
