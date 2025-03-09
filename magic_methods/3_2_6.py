class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        ans = request.get('method', 'GET')
        if ans != 'GET':
            return
        return self.get(self.func, request)

    def get(self, func, request, *args, **kwargs):
        s = func(request)
        return f"GET: {s}"
