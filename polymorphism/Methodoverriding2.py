class Parent:
    def property(self):
        print("**** P-Gold, P-Land, P-House , P-Cash ****")


class Child(Parent):
    def property(self):
        super().property()
        print("**** C-Gold, C-Land, C-House , C-Cash ****")


child=Child()
child.property()

