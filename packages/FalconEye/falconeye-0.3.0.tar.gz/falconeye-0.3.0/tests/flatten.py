from FalconEye import Flatten
print(Flatten({}).items)
print(Flatten({"Hello": "World!"}).items)
print(Flatten({"OuterKey": {"Test1": "Operable", "InnerKey": {"Test2": ["Operable", "Operable"], "Test3": "Operable"}}}).items)