import abc


class SpartaCache(abc.ABC):
    def __init__(
        self,
        key_prefix=None,
    ):
        self.key_prefix = key_prefix if isinstance(key_prefix, str) else str(key_prefix)

    def _map_key(self, key):
        return self.key_prefix + key if self.key_prefix else key

    @abc.abstractmethod
    def add(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def append(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def cas(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def decr(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def gets(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def incr(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def prepend(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def replace(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def touch(self, key, *args, **kwargs):
        pass

    def atomic_append(self, key, value, _retries=3, *args, **kwargs):
        """
        Required cas behavior!
        Assures atomic append to a list of objects (only tuple is supported, not list).
        Solution copied from https://stackoverflow.com/a/27468294/20230162
        """
        try:
            _values, cas_id = self.gets(key)
        except ValueError as e:
            raise RuntimeError("atomic_append requires cas behavior") from e
        if _values is None:
            self.set(key, (value,), *args, **kwargs)
        else:
            if value not in _values:
                ok = self.cas(key, _values + (value,), cas_id, *args, **kwargs)
                if not ok and _retries > 1:
                    self.atomic_append(key, value, _retries - 1, *args, **kwargs)
