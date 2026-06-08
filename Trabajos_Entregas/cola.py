class Queue:
    """Clase para el TDA Cola (FIFO - First In, First Out)"""

    def __init__(self):
        self.__elements = []

    def arrive(self, value):
        """Agrega un elemento al final de la cola."""
        self.__elements.append(value)

    def attention(self):
        """Quita y retorna el elemento que está al frente de la cola."""
        if not self.is_empty():
            return self.__elements.pop(0)
        else:
            return None

    def on_front(self):
        """Retorna el elemento que está al frente sin quitarlo."""
        if not self.is_empty():
            return self.__elements[0]
        else:
            return None

    def is_empty(self):
        """Devuelve True si la cola está vacía."""
        return len(self.__elements) == 0

    def size(self):
        """Devuelve la cantidad de elementos en la cola."""
        return len(self.__elements)

    def move_to_end(self):
        """Mueve el elemento del frente al final (útil para barridos)."""
        if not self.is_empty():
            self.arrive(self.attention())