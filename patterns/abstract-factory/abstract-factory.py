class IceCreamFactory:
    def get_ice_cream(self):
        pass


class ChocolateIceCream(IceCreamFactory):
    def get_ice_cream(self):
        return "It's a chocolate ice-cream."


class VanillaIceCream(IceCreamFactory):
    def get_ice_cream(self):
        return "It's a vanilla ice-cream."
    

class BoxFactory:
    def get_box(self):
        pass


class SquareBox(BoxFactory):
    def get_box(self):
        return "It's a square box."


class RoundBox(BoxFactory):
    def get_box(self):
        return "It's a round box."
    

class IceCreamBox:
    def get_ice_cream():
        pass
    def get_box():
        pass


class ChocolateIceCreamBox(IceCreamBox):
    def get_ice_cream(self):
        return ChocolateIceCream()
    def get_box(self):
        return SquareBox()


class VanillaIceCreamBox(IceCreamBox):
    def get_ice_cream(self):
        return VanillaIceCream()

    def get_box(self):
        return RoundBox()
    

class IceCreamShop:
    def __init__(self, factory: IceCreamBox) -> None:
        self.ice_cream:IceCreamFactory = factory.get_ice_cream()
        self.box:IceCreamBox = factory.get_box()
    
    def get_ice_cream(self):
        return self.ice_cream.get_ice_cream()

    def get_box(self):
        return self.box.get_box()


chocolateIceCreamBoxFactory = ChocolateIceCreamBox()
chocolateIceCream = IceCreamShop(chocolateIceCreamBoxFactory)
print(chocolateIceCream.get_ice_cream())
print(chocolateIceCream.get_box())


vanillaIceCreamBoxFactory = VanillaIceCreamBox()
vanillaIceCream = IceCreamShop(vanillaIceCreamBoxFactory)
print(vanillaIceCream.get_ice_cream())
print(vanillaIceCream.get_box())
