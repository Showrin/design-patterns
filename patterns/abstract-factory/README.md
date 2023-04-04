# Abstract Factory

## What is it?

Abstract factory pattern is a creational design pattern that creates families of related or dependent products. This pattern is usually implemented using a set of factory methods.

For example, we have a ice-cream factory that produces different flavored ice-creams. And we also have a factory that produces different type of ice-cream boxes. Then we have an ice-cream shop (abstract class) that can produce different different ice-creams with combinations of ice-creams and boxes.

## Implementation

### Implementation in Python

```
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

```
