# Abstract Factory

## What is it?

Abstract factory pattern is a creational design pattern that is useful when a single factory is not enough to implement our desired feature.

## When should we use it?

1. a system should be independent of how its products are created, composed, and represented.
2. a system should be configured with one of multiple families of products.
3. a family of related product objects is designed to be used together, and you need to enforce this constraint.
4. you want to provide a class library of products, and you want to reveal just their interfaces, not their implementations.

## Real Life use case

We can think of axios as an example of this pattern.

1. axios **[Abstract Factory]**
   1. Get **[Request Factory]**
      1. Request with params
      2. Request without params
      3. Request with auth token
      4. ...
   2. Post **[Request Factory]**
   3. Put **[Request Factory]**
   4. Delete **[Request Factory]**

## Implementation

### Implementation in Python

```
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

```

#### Output

```
Windows button has been clicked!
Windows Input has been focused!
Mac button has been clicked!
Mac Input has been focused!
```
