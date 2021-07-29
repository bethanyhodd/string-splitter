import re


class TagManipulator():
    def parse_string(self, tags, regex=","):
        result = []

        tempResult = re.split(regex, tags)
        if(len(tempResult[0]) > 0):
            result = tempResult
        else:
            for i in tempResult:
                if i != "":
                    result.append(i)
        return result
