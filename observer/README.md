# Observer Pattern

Observer is a behavioral pattern that lets users implement a subscription mechanism to notify multiple objects about any events that happen to the object they're observing or listening. Kind of a pub-sub architecture.

## Real life use cases

1. Uber/Pathao notifications
2. Websocket communication (Socket.io)
3. State update and re-render in React
4. Event listener in JS

## Implementation

### Observer in Python

```
from typing import List


class Subscriber:
    _name = None

    def __init__(self, name) -> None:
        self._name = name

    def paint_data(self, data):
        print(f"Hello, {self._name} speaking. Received {data}.")


class Publisher:
    _subscribers: List[Subscriber] = []

    def add_subscriber(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)

    def notify_subscriber(self):
        data = "Data from publisher"

        for subscriber in self._subscribers:
            subscriber.paint_data(data)


publisher = Publisher()

subscriber_1 = Subscriber("Sub_1")
subscriber_2 = Subscriber("Sub_2")
subscriber_3 = Subscriber("Sub_3")

publisher.add_subscriber(subscriber_1)
publisher.add_subscriber(subscriber_2)
publisher.add_subscriber(subscriber_3)

publisher.notify_subscriber()

```

#### Output

```
Hello, Sub_1 speaking. Received Data from publisher.
Hello, Sub_2 speaking. Received Data from publisher.
Hello, Sub_3 speaking. Received Data from publisher.
```

### Observer pattern in JS

```
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

```

#### Output

```
Hello, Sub_1 speaking. Received Data from publisher.
Hello, Sub_2 speaking. Received Data from publisher.
Hello, Sub_3 speaking. Received Data from publisher.

```
