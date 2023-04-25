# Adapter Pattern

## What is it?

Adapter pattern is a structural design pattern that helps us to collaborate between objects with incompatible interfaces.

Suppose, you have a mobile that needs a USB C (male) type ports to connect external memories with your phone. You have a pendrive. Unfortunately the pendrive has USB A (male) type port that is incompatible with the phone. Now what can we do here?

Yes, we can search for an adapter that has USB A (female) and USB C (male) port so that we can connect our pendrive with that adapter and the adapter with our phone. This is the ultimate adapter design pattern.

## Implementation

### Implementation in Python

```
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

```

#### Output

```
Output:
Reading data from the pendrive...
Pendrive data = > {'usb_a': 'This is pendrive data'}
....
Converting USB A(male) to USB C(male) input...
Adapter output data = > {'usb_c': 'This is pendrive data'}
....
Phone read data = > This is pendrive data
```

### Implementation in JS

```
class PendriveAdapter {
	convert_usb_a_to_usb_c(data) {
		console.log("Converting USB A (male) to USB C (male) input...");

		if (data["usb_a"]) {
			return {
				usb_c: data["usb_a"],
			};
		}

		throw Error("Invalid data provided to the adapter.");
	}
}

class Phone {
	read_external_memory_data(data) {
		if (data["usb_c"]) {
			return data["usb_c"];
		}

		throw Error("Invalid data provided to the phone.");
	}
}

class Pendrive {
	constructor(data) {
		this.data = data;
	}

	get_data() {
		console.log("Reading data from the pendrive...");

		return {
			usb_a: this.data,
		};
	}
}

const pendrive = new Pendrive("This is pendrive data");
const pendrive_data = pendrive.get_data();
console.log(`Pendrive data => ${JSON.stringify(pendrive_data)}\n....`);

const adapter = new PendriveAdapter();
const converted_data = adapter.convert_usb_a_to_usb_c(pendrive_data);
console.log(`Adapter output data => ${JSON.stringify(converted_data)}\n....`);

const phone = new Phone();
const phone_data = phone.read_external_memory_data(converted_data);
console.log(`Phone read data => ${phone_data}`);

```

#### Output

```
Output:
Reading data from the pendrive...
Pendrive data => {"usb_a":"This is pendrive data"}
....
Converting USB A (male) to USB C (male) input...
Adapter output data => {"usb_c":"This is pendrive data"}
....
Phone read data => This is pendrive data
```
