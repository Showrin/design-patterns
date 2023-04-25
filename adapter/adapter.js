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

// Output:
// Reading data from the pendrive...
// Pendrive data =>{"usb_a":"This is pendrive data"}
// ....
// Converting USB A (male) to USB C (male) input...
// Adapter output data => {"usb_c":"This is pendrive data"}
// ....
// Phone read data => This is pendrive data
