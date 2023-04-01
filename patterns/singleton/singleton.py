class SettingsManager:
    __instance = None

    def __init__(self, settings) -> None:
        if self.__instance:
            SettingsManager.__instance = self.__instance
        else:
            SettingsManager.__instance = settings

    def get_settings(self) -> str:
        return str(self.__instance)

    def set(self, key: str, value) -> None:
        self.__instance[key] = value


a = SettingsManager({})
a.set("name", "Showrin")

b = SettingsManager({})
b.set("id", "1234")

# a & b will display the same instance dictionary
print(a.get_settings(), b.get_settings())

# Output
# {'name': 'Showrin', 'id': '1234'} {'name': 'Showrin', 'id': '1234'}
