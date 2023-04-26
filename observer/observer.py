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

# Output
# Hello, Sub_1 speaking. Received Data from publisher.
# Hello, Sub_2 speaking. Received Data from publisher.
# Hello, Sub_3 speaking. Received Data from publisher.
