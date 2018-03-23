from collections import UserList


class RecursiveList(UserList):

    def __getitem__(self, index):
        if index >= len(self):
            index = index - len(self)
        return super().__getitem__(index)
