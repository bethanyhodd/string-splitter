import re


class TagManipulator():
    def parse_string(self, tags, regex=",\\ *"):
        result = []

        tempResult = re.split(regex, tags)

        for i in tempResult:
            if not i == "":
                result.append(i)
        return result
