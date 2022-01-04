import requests
from pprint import pprint
def get_questions():
    url = "https://api.stackexchange.com/2.3/questions?fromdate=1640995200&todate=1641168000&order=desc&min=1640995200&max=1641168000&sort=activity&tagged=Python&site=stackoverflow"
    response = requests.get(url)
    pprint (response.json())
get_questions()