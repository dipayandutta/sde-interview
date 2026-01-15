class SimpleMeta(type):
    def __new__(cls,name,bases,namespace):
        print(f"[Meta] Creaing Class: {name}")

        if 'version' not in namespace:
            raise TypeError(f"{name} must define 'version'")

        namespace['get_version'] = lambda self: self.version

        return super().__new__(cls,name,bases,namespace)

class App(metaclass=SimpleMeta):
    version = "1.0"
    def run(self):
        print("Application Running")

app = App()
app.run()
print(app.get_version())
