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

// Output
// Preparing your ice-cream. Please, wait a while .
// You have ordered for a mix of Blackforest and Butterscotch.
//
// Preparing your ice-cream. Please, wait a while .
// You have ordered for a mix of Butterscotch and Chocolate.
