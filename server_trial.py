class Server:
    """для описания работы серверов в сети
    Соответственно в объектах класса Server должны быть локальные свойства:
    buffer - список принятых пакетов (изначально пустой);
    ip - IP-адрес текущего сервера.
    """
    __server_ip_instance = 0

    def __init__(self):
        type(self).__server_ip_instance += 1
        self.ip = self.__server_ip_instance
        self.buffer = list()
        self.links_with_rt = {self.ip: []}

    def send_data(self, data):
        """для отправки информационного пакета data (объекта класса Data)
        с указанным IP-адресом получателя (пакет отправляется роутеру и
        сохраняется в его буфере - локальном свойстве buffer);
        """
        if isinstance(data, Data):
            routers = self.links_with_rt[self.ip]
            for rt in routers:
                rt.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов (если ничего принято не было,
        то возвращается пустой список) и очищает входной буфер;
        """
        show = self.buffer.copy()
        self.buffer.clear()
        return show

    def get_ip(self):
        """возвращает свой IP-адрес.
        """
        return self.ip


class Router:
    """для описания работы роутеров в сети (в данной задаче полагается один роутер).
    И одно обязательное локальное свойство (могут быть и другие свойства):
    buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
    """
    __router_ip_instance = 0

    def __init__(self):
        type(self).__router_ip_instance += 1
        self.router_ip = self.__router_ip_instance
        self.buffer = list()
        self.links_with_serv = {self.router_ip: []}

    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру
        """
        if isinstance(server, Server):
            server.links_with_rt[server.ip].append(self)
            self.links_with_serv[self.router_ip].append(server)
            return

    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера
        """
        if isinstance(server, Server):
            if server in self.links_with_serv[self.router_ip]:
                self.links_with_serv[self.router_ip].remove(server)
                server.links_with_rt[server.ip].remove(self)
                return

    def has_connection(self, data):
        if isinstance(data, Data):
            for srv in self.links_with_serv[self.router_ip]:
                if data.to_ip == srv.ip:
                    data.ready_to_send = True
                    return True
            return False

    def send_data(self):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера
        соответствующим серверам (после отправки буфер должен очищаться)
        """
        for data in self.buffer:
            if self.has_connection(data):
                for srv in self.links_with_serv[self.router_ip]:
                    if data.to_ip == srv.ip:
                        srv.buffer.append(data)
        self.buffer.clear()


class Data:
    """для описания пакета информации
    Наконец, объекты класса Data должны содержать, два следующих локальных свойства:
    data - передаваемые данные (строка);
    ip - IP-адрес назначения.
    """

    def __init__(self, data_message, destination_ip):
        self.data = data_message
        self.to_ip = destination_ip
        self.ready_to_send = False
