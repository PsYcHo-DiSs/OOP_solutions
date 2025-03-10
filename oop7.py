class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots
        self.mem_slots = mem_slots[:total_mem_slots]

    def get_config(self):
        return [f"Материнская плата: {self.name}",
                f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
                f"Слотов памяти: {self.total_mem_slots}",
                f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}"
                ]


cpu = CPU('intel', 1333)
mem1, mem2 = Memory('Samsung', 4000), Memory('Samsung', 4000)
mb = MotherBoard('asus', cpu, [mem1, mem2])
print(mb.get_config())
