# Factory Pattern

## What is it?

It's a creational pattern that is mainly used to reduce the overhead of creating different type of objects. In this pattern a class called factory takes inputs from the user and based on these inputs it decides which class' instance has to be created.

Suppose, you've gone to a ice-cream shop and there's a lot of ice-creams kept in different trays. Now, think, if it was a self service, like you had to take ice-creams of your taste, it would be a bit hectic. Isn't it?

To reduce this overhead what these businesses do is they keep a person to make ice-cream of your choice mixing multiple ice-creams from the tray and serve you. Here's that person is our factory class and this work pattern represents the factory design pattern.

## Implementation

### Factory pattern in JS

```
const Blackforest_Butterscotch = "blackforest-butterscotch";
const Butterscotch_Chocolate = "blackforest-chocolate";

class IceCream {
	constructor() {
		this.waitingMessage = "Preparing your ice-cream. Please, wait a while.";
	}

	get() {
		return this.waitingMessage;
	}
}

class BlackforestButterscotchMix extends IceCream {
	constructor() {
		super();

		this.orderConfirmationMessage =
			"You have ordered for a mix of Blackforest and Butterscotch.";
	}

	get() {
		return `${this.waitingMessage}\n${this.orderConfirmationMessage}\n`;
	}
}

class ButterscotchChocolateMix extends IceCream {
	constructor() {
		super();

		this.orderConfirmationMessage =
			"You have ordered for a mix of Butterscotch and Chocolate.";
	}

	get() {
		return `${this.waitingMessage}\n${this.orderConfirmationMessage}\n`;
	}
}

class IceCreamFactory {
	makeIceCream(mixingType) {
		if (mixingType === Blackforest_Butterscotch) {
			return new BlackforestButterscotchMix();
		}

		if (mixingType === Butterscotch_Chocolate) {
			return new ButterscotchChocolateMix();
		}
	}
}

const blackforestButterscotchMixIceCream = new IceCreamFactory().makeIceCream(
	Blackforest_Butterscotch
);
console.log(blackforestButterscotchMixIceCream.get());

const butterscotchChocolateMixIceCream = new IceCreamFactory().makeIceCream(
	Butterscotch_Chocolate
);
console.log(butterscotchChocolateMixIceCream.get());

```

#### Output

```
Preparing your ice-cream. Please, wait a while .
You have ordered for a mix of Blackforest and Butterscotch.

Preparing your ice-cream. Please, wait a while .
You have ordered for a mix of Butterscotch and Chocolate.
```

### Factory pattern in Python

```
Blackforest_Butterscotch = "blackforest-butterscotch"
Butterscotch_Chocolate = "blackforest-chocolate"


class IceCream:
    def __init__(self) -> None:
        self.waiting_message = "Preparing your ice-cream. Please, wait a while."

    def get(self) -> str:
        return self.waiting_message


class BlackforestButterscotchMix(IceCream):
    def __init__(self) -> None:
        super().__init__()

        self.order_confirmation_message = "You have ordered for a mix of Blackforest and Butterscotch.\n"

    def get(self) -> str:
        return f"{self.waiting_message}\n{self.order_confirmation_message}"


class ButterscotchChocolateMix(IceCream):
    def __init__(self) -> None:
        super().__init__()

        self.order_confirmation_message = "You have ordered for a mix of Butterscotch and Chocolate."

    def get(self) -> str:
        return f"{self.waiting_message}\n{self.order_confirmation_message}\n"


class IceCreamFactory:
    @staticmethod
    def make_ice_cream(mixing_type):
        if mixing_type == Blackforest_Butterscotch:
            return BlackforestButterscotchMix()

        if mixing_type == Butterscotch_Chocolate:
            return ButterscotchChocolateMix()


blackforest_butterscotch_mix_ice_cream = IceCreamFactory.make_ice_cream(
    Blackforest_Butterscotch)
print(blackforest_butterscotch_mix_ice_cream.get())

butterscotch_chocolate_mix_ice_cream = IceCreamFactory.make_ice_cream(
    Butterscotch_Chocolate)
print(butterscotch_chocolate_mix_ice_cream.get())

```

#### Output

```
Preparing your ice-cream. Please, wait a while .
You have ordered for a mix of Blackforest and Butterscotch.

Preparing your ice-cream. Please, wait a while .
You have ordered for a mix of Butterscotch and Chocolate.
```
