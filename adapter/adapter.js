class Serializer {
	data = null;

	constructor({ obj, data }) {
		if (obj) {
			this.data = this.convert_to_json(obj);
		} else if (data) {
			this.data = this.convert_to_object(data);
		}
	}

	convert_to_json(obj) {
		console.log("Converted JS Object to JSON.");
		return `${obj} in json format`;
	}

	convert_to_object(data) {
		console.log("Converted JSON to JS Object.");
		return `${data} in object format`;
	}
}

class ApiView {
	list(request) {
		const data = request["data"];

		const serialized_request_data = new Serializer({ data }).data;
		console.log(serialized_request_data);

		console.log("-------------------------");
		const excepted_result = "Expected result";

		const serialized_response_data = new Serializer({ obj: excepted_result })
			.data;
		console.log(serialized_response_data);

		return serialized_response_data;
	}
}

const list_api_view = new ApiView().list({ data: "Request body" });

// Output
// Converted JSON to JS Object.
// Request body in object format
// -------------------------
// Converted JS Object to JSON.
// Expected result in json format

// class PendriveAdapter {
// 	convert_usb_a_to_usb_c(data) {
// 		console.log("Converting USB A (male) to USB C (male) input...");

// 		if (data["usb_a"]) {
// 			return {
// 				usb_c: data["usb_a"],
// 			};
// 		}

// 		throw Error("Invalid data provided to the adapter.");
// 	}
// }

// class Phone {
// 	read_external_memory_data(data) {
// 		if (data["usb_c"]) {
// 			return data["usb_c"];
// 		}

// 		throw Error("Invalid data provided to the phone.");
// 	}
// }

// class Pendrive {
// 	constructor(data) {
// 		this.data = data;
// 	}

// 	get_data() {
// 		console.log("Reading data from the pendrive...");

// 		return {
// 			usb_a: this.data,
// 		};
// 	}
// }

// const pendrive = new Pendrive("This is pendrive data");
// const pendrive_data = pendrive.get_data();
// console.log(`Pendrive data => ${JSON.stringify(pendrive_data)}\n....`);

// const adapter = new PendriveAdapter();
// const converted_data = adapter.convert_usb_a_to_usb_c(pendrive_data);
// console.log(`Adapter output data => ${JSON.stringify(converted_data)}\n....`);

// const phone = new Phone();
// const phone_data = phone.read_external_memory_data(converted_data);
// console.log(`Phone read data => ${phone_data}`);

// Output:
// Reading data from the pendrive...
// Pendrive data =>{"usb_a":"This is pendrive data"}
// ....
// Converting USB A (male) to USB C (male) input...
// Adapter output data => {"usb_c":"This is pendrive data"}
// ....
// Phone read data => This is pendrive data
