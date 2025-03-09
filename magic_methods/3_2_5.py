class RenderList:
    def __init__(self, type_list):
        # if type_list not in ('ul', 'ol'):
        #     self.type_list = 'ul'
        self.type_list = type_list

    def __setattr__(self, key, value):
        if key == 'type_list' and value not in ('ul', 'ol'):
            super().__setattr__(key, 'ul')
        else:
            super().__setattr__(key, value)

    def __call__(self, data, *args, **kwargs):
        data_formation = '\n'.join(f'<li>{elem}</li>' for elem in data)
        return f"<{self.type_list}>\n{data_formation}\n</{self.type_list}>"


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("-")
html = render(lst)

print(html)
