class Graph:
    def __init__(self, data):
        self.data = data.copy()
        self.is_show = True
        self.s = ' '.join(map(str, self.data))

    def set_data(self, data):
        self.data = data.copy()
        self.s = ' '.join(map(str, self.data))

    def show_table(self):
        if self.is_show:
            print(self.s)
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show:
            print(f"Графическое отображение данных: {self.s}")
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show:
            print(f"Столбчатая диаграмма: {self.s}")
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
