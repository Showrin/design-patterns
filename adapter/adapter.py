class Serializer:
    data = None

    def __init__(self, obj=None, data=None) -> None:
        if obj:
            self.data = self.convert_to_json(obj)
        elif data:
            self.data = self.convert_to_object(data)

    def convert_to_json(self, obj):
        print("Converted Python Object to JSON.")
        return f"{obj} in json format"

    def convert_to_object(self, data):
        print("Converted JSON to Python Object.")
        return f"{data} in object format"


class ApiView:
    def list(self, request):
        data = request["data"]

        serialized_request_data = Serializer(data=data).data
        print(serialized_request_data)

        print("-------------------------")
        excepted_result = "Expected result"

        serialized_response_data = Serializer(excepted_result).data
        print(serialized_response_data)

        return serialized_response_data


list_api_view = ApiView().list(request={
    "data": "Request body"
})

# Output
# Converted JSON to Python Object.
# Request body in object format
# -------------------------
# Converted Python Object to JSON.
# Expected result in json format


# class PendriveAdapter:
#     def convert_usb_a_to_usb_c(self, data):
#         print("Converting USB A (male) to USB C (male) input...")

#         if data['usb_a']:
#             return {
#                 'usb_c': data['usb_a']
#             }

#         raise ValueError("Invalid data provided to the adapter.")


# class Phone:
#     def read_external_memory_data(self, data: dict):
#         if data['usb_c']:
#             return data['usb_c']

#         raise ValueError("Invalid data provided to the phone.")


# class Pendrive:
#     def __init__(self, data) -> None:
#         self.data = data

#     def get_data(self):
#         print("Reading data from the pendrive...")

#         return {
#             'usb_a': self.data
#         }


# pendrive = Pendrive("This is pendrive data");
# pendrive_data = pendrive.get_data()
# print(f"Pendrive data => {pendrive_data}\n....")

# adapter = PendriveAdapter()
# converted_data = adapter.convert_usb_a_to_usb_c(pendrive_data)
# print(f"Adapter output data => {converted_data}\n....")

# phone = Phone()
# phone_data = phone.read_external_memory_data(converted_data)
# print(f"Phone read data => {phone_data}")

# Output:
# Reading data from the pendrive...
# Pendrive data = > {'usb_a': 'This is pendrive data'}
# ....
# Converting USB A(male) to USB C(male) input...
# Adapter output data = > {'usb_c': 'This is pendrive data'}
# ....
# Phone read data = > This is pendrive data
