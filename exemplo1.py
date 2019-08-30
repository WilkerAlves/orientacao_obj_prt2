class Queue:
    """
        Abstração de qualquer tipo de fila:
            - supermercado
            - processos
    """

    c_queue = []

    def __init__(self):
        self.s_queue = []

    @classmethod
    def c_get_in_line(cls, obj):
        cls.c_queue.append(obj)
        print(cls.c_queue)

    def s_get_in_line(self, obj):
        self.s_queue.append(obj)
        print(self.c_queue)
