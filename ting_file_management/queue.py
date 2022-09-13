class Queue:
    def __init__(self):
      self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        current_data = self._data[0]
        del self._data[0]
        return current_data

    def search(self, index):
        if index in range(self.__len__()):
          return self._data[index]
        raise IndexError
