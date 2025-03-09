class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, name, *args, **kwargs):
        point_indx = name.rfind('.')
        ext = "" if point_indx == -1 else name[point_indx+1:]
        return ext in self.extensions
