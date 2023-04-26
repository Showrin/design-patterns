class Subscriber {
	name = null;

	constructor(name) {
		this._name = name;
	}

	paintData(data) {
		console.log(`Hello, ${this._name} speaking. Received ${data}.`);
	}
}

class Publisher {
	_subscribers = [];

	addSubscriber(subscriber) {
		this._subscribers.push(subscriber);
	}

	notifySubscriber() {
		const data = "Data from publisher";

		this._subscribers.forEach((subscriber) => subscriber.paintData(data));
	}
}

const publisher = new Publisher();

const subscriber1 = new Subscriber("Sub_1");
const subscriber2 = new Subscriber("Sub_2");
const subscriber3 = new Subscriber("Sub_3");

publisher.addSubscriber(subscriber1);
publisher.addSubscriber(subscriber2);
publisher.addSubscriber(subscriber3);

publisher.notifySubscriber();

// Output
// Hello, Sub_1 speaking. Received Data from publisher.
// Hello, Sub_2 speaking. Received Data from publisher.
// Hello, Sub_3 speaking. Received Data from publisher.
