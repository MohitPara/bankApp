from abc import ABC, abstractmethod


class IOperations(ABC):
    @abstractmethod
    def create_acc(self):
        pass

    @abstractmethod
    def update_acc(self):
        pass

    @abstractmethod
    def delete_acc(self):
        pass

    @abstractmethod
    def deposit_mony(self):
        pass

    @abstractmethod
    def withwrew_mony(self):
        pass

    @abstractmethod
    def acc_detail(self):
        pass


class IoP(ABC):
    pass
