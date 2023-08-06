from FalconEye import Walk
print(Walk({}).items)
print(Walk({"Hello": "World!"}).items)
print(Walk({"OuterKey": {"Test1": "Operable", "InnerKey": {"Test2": ["Operable", "Operable"], "Test3": "Operable"}}}).items)