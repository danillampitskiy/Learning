class KeyValueStorage:
    def __init__(self, file_path):
        self.data = {}
        self._load_data(file_path)

    def _load_data(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                key, value = line.split('=', 1)
                if value.isdigit():
                    value = int(value)
                self.data[key] = value

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        elif key in self.data:
            return self.data[key]
        else:
            raise AttributeError(f"'KeyValueStorage' object has no attribute '{key}'")

    def __getitem__(self, key):
        return self.data[key]


# Usage example
storage = KeyValueStorage('path_to_file.txt')

# Accessing values using collection items and attributes
print(storage['name'])
print(storage.song)
print(storage.power)

# Attempting to access an unknown attribute should raise an error
try:
    print(storage.unknown_key)
except AttributeError as e:
    print(str(e))  # Output: "'KeyValueStorage' object has no attribute 'unknown_key'"