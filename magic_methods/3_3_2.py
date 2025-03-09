class Model:
    def __init__(self):
        self.data = dict()

    def query(self, **kwargs):
        self.data.update(**kwargs)

    def __str__(self):
        if self.data:
            data_to_s = 'Model: '
            for field, value in self.data.items():
                data_to_s += f"{field} = {value}, "
        else:
            data_to_s = "Model"

        return data_to_s.rstrip(', ')
