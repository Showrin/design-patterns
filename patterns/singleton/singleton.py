class SettingsManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


a = SettingsManager()
a.color = "red"

b = SettingsManager()
b.color = "blue"

# a & b will display the same instance dictionary
print(a.color)
print(b.color)
print(a is b)

# Output
# blue
# blue
# True
