class PendriveAdapter:
    def convert_usb_a_to_usb_c(self, data):
        print("Converting USB A (male) to USB C (male) input...")

        if data['usb_a']:
            return {
                'usb_c': data['usb_a']
            }
        
        raise ValueError("Invalid data provided to the adapter.")
    

class Phone:
    def read_external_memory_data(self, data: dict):
        if data['usb_c']:
            return data['usb_c']
        
        raise ValueError("Invalid data provided to the phone.")
    

class Pendrive:
    def __init__(self, data) -> None:
        self.data = data

    def get_data(self):
        print("Reading data from the pendrive...")

        return {
            'usb_a': self.data
        }
    

pendrive = Pendrive("This is pendrive data");
pendrive_data = pendrive.get_data()
print(f"Pendrive data => {pendrive_data}\n....")

adapter = PendriveAdapter()
converted_data = adapter.convert_usb_a_to_usb_c(pendrive_data)
print(f"Adapter output data => {converted_data}\n....")

phone = Phone()
phone_data = phone.read_external_memory_data(converted_data)
print(f"Phone read data => {phone_data}")

# Output:
# Reading data from the pendrive...
# Pendrive data = > {'usb_a': 'This is pendrive data'}
# ....
# Converting USB A(male) to USB C(male) input...
# Adapter output data = > {'usb_c': 'This is pendrive data'}
# ....
# Phone read data = > This is pendrive data
