import abc


class CorePlatform(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_shortcut(self, path, target):
        pass

    @abc.abstractmethod
    def add_to_path(self, path):
        pass