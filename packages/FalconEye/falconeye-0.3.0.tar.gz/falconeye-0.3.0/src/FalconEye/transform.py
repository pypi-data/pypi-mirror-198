import pandas as pd
import uuid
from .flatten import Flatten


class FalconFrame():
    def __init__(self, obj):
        if isinstance(obj, list) or isinstance(obj, dict):
            self.df = pd.DataFrame.from_dict(obj)  # type: ignore
        elif isinstance(obj, pd.DataFrame):
            self.df = obj
        else:
            raise TypeError(
                "obj argument must be a dictionary, list of dictionaries, or dataframe")

    def transform(self, pk=None, callback=None, fields=[], inplace=False, calculatedFields=[]):
        if fields and callback:
            rows = self.df.to_dict(orient="records")

            def makeKey(current=[], pk=pk):
                if current:
                    last = current[-1]
                else:
                    last = 0
                if pk == None:
                    newKey = last + 1
                elif pk == "uuid":
                    newKey = uuid.uuid4()
                else:
                    raise Exception("PK argument must be None or uuid")
                current.append(newKey)
                return current, newKey
            newData = []
            currentKeys = []
            for row in rows:
                for field in fields:
                    rowSet = {}
                    keySet, newKey = makeKey(currentKeys)
                    currentKeys = keySet
                    rowSet["pk"] = newKey
                    for fieldSet in row:
                        if fieldSet not in fields:
                            rowSet[fieldSet] = row[fieldSet]
                        else:
                            continue
                    for calculatedField in calculatedFields:
                        rowSet[calculatedField] = calculatedFields[calculatedField](
                            row)
                    call = callback(field, row[field])
                    if not call:
                        continue
                    for key, value in call.items():
                        rowSet[key] = value
                    newData.append(rowSet)
            if inplace:
                self.df = pd.DataFrame.from_dict(newData)  # type: ignore
                return self
            else:
                # type: ignore
                return FalconFrame(newData)
        elif calculatedFields:
            pass
        else:
            raise Exception(
                "Fields and Callback argument must be used in leiu of calculatedFields argument")
