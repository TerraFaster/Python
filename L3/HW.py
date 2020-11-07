import requests
from typing import Union

class EnginePattern:
    def __init__(self):
        pass

    def sendRequest(self):
        pass

class CrawlerPattern:
    def __init__(self):
        pass

    def getPageData(self):
        pass

class ParserPattern:
    def __init__(self):
        pass

    def getPageData(self):
        pass


class Engine(EnginePattern):
    def __init__(self):
        self.r = None

    def sendRequest(self, number: Union[int, str]):
        try:
            self.r = requests.get(f"http://numbersapi.com/{number}")

        except requests.ConnectionError as e:
            self.r = None
            raise ConnectionError("No connection.")

        return self.r


class Crawler(CrawlerPattern):
    def __init__(self):
        self.number = None
        self.data = None

    def getPageData(self, number: Union[int, str] = 0):
        self.number = number

        r = self.Engine.sendRequest(self.number)

        self.data = r.content

        return self.data


class Parser(ParserPattern):
    def __init__(self):
        self.crawler = Crawler()
        self.data = None
        self.parsedData = None

    def parse(self, number: Union[int, str]):
        self.data = self.crawler.getPageData(number)

        self.parsedData = self.data.decode("utf-8")

        return self.parsedData


p = Parser()

print(p.parse(int(input("Введите номер: "))))