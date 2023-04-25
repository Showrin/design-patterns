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


# Output
# Preparing your ice-cream. Please, wait a while .
# You have ordered for a mix of Blackforest and Butterscotch.
#
# Preparing your ice-cream. Please, wait a while .
# You have ordered for a mix of Butterscotch and Chocolate.
