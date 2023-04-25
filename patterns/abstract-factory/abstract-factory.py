class Btn:
    def click(self):
        pass


class WinBtn(Btn):
    def click(self):
        print("Windows button has been clicked!")


class MacBtn(Btn):
    def click(self):
        print("Mac button has been clicked!")


class Input:
    def focus(self):
        pass


class WinInput(Input):
    def focus(self):
        print("Windows Input has been focused!")


class MacInput(Input):
    def focus(self):
        print("Mac Input has been focused!")


class UiFactory:
    def createBtn(self):
        pass

    def createInput(self):
        pass


class WinUiFactory(UiFactory):
    def createBtn(self) -> Btn:
        return WinBtn()

    def createInput(self) -> Input:
        return WinInput()


class MacUiFactory(UiFactory):
    def createBtn(self) -> Btn:
        return MacBtn()

    def createInput(self) -> Input:
        return MacInput()


class AppFactory:
    def __init__(self, os_ui_factory: WinUiFactory) -> None:
        self.btn = os_ui_factory.createBtn()
        self.input = os_ui_factory.createInput()

    def execute(self) -> None:
        self.btn.click()
        self.input.focus()


win_ui_factory = WinUiFactory()
app_factory = AppFactory(win_ui_factory)

app_factory.execute()

mac_ui_factory = MacUiFactory()
app_factory = AppFactory(mac_ui_factory)

app_factory.execute()


# class IceCreamFactory:
#     def get_ice_cream(self):
#         pass


# class ChocolateIceCream(IceCreamFactory):
#     def get_ice_cream(self):
#         return "It's a chocolate ice-cream."


# class VanillaIceCream(IceCreamFactory):
#     def get_ice_cream(self):
#         return "It's a vanilla ice-cream."


# class BoxFactory:
#     def get_box(self):
#         pass


# class SquareBox(BoxFactory):
#     def get_box(self):
#         return "It's a square box."


# class RoundBox(BoxFactory):
#     def get_box(self):
#         return "It's a round box."


# class IceCreamBox:
#     def get_ice_cream():
#         pass
#     def get_box():
#         pass


# class ChocolateIceCreamBox(IceCreamBox):
#     def get_ice_cream(self):
#         return ChocolateIceCream()
#     def get_box(self):
#         return SquareBox()


# class VanillaIceCreamBox(IceCreamBox):
#     def get_ice_cream(self):
#         return VanillaIceCream()

#     def get_box(self):
#         return RoundBox()


# class IceCreamShop:
#     def __init__(self, factory: IceCreamBox) -> None:
#         self.ice_cream:IceCreamFactory = factory.get_ice_cream()
#         self.box:IceCreamBox = factory.get_box()

#     def get_ice_cream(self):
#         return self.ice_cream.get_ice_cream()

#     def get_box(self):
#         return self.box.get_box()


# chocolateIceCreamBoxFactory = ChocolateIceCreamBox()
# chocolateIceCream = IceCreamShop(chocolateIceCreamBoxFactory)
# print(chocolateIceCream.get_ice_cream())
# print(chocolateIceCream.get_box())


# vanillaIceCreamBoxFactory = VanillaIceCreamBox()
# vanillaIceCream = IceCreamShop(vanillaIceCreamBoxFactory)
# print(vanillaIceCream.get_ice_cream())
# print(vanillaIceCream.get_box())
