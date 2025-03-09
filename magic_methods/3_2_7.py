class Handler:
    def __init__(self, methods):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            if not request:
                method = 'GET'
            elif not request['method']:
                method = 'GET'
            else:
                method = request['method']

            if method not in self.methods:
                return
            method = method.lower()
            return self.__getattribute__(method)(func, request)

        return wrapper

    def get(self, func, request, *args, **kwargs):
        s = func(request)
        return f"GET: {s}"

    def post(self, func, request, *args, **kwargs):
        s = func(request)
        return f"POST: {s}"