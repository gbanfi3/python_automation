class ClassTest:
    def instance_method(self):
        print(f"instance_method of {self}")

    @classmethod
    def klass_method(cls):
        print(f"called class_method of {cls}")

    @staticmethod
    def stat_method():
        print(f"called static method ")


a = ClassTest()
a.instance_method()
ClassTest.instance_method(a)

ClassTest.klass_method()

ClassTest.stat_method()