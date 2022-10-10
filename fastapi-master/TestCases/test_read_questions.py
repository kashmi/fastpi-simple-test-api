import json
import jsonpath
import requests
# import app.api.api

baseUrl = 'http://127.0.0.1:8000'

def test_read_question():
    with open('data/questions.json') as stream:
        inputData = json.load(stream)
    path = '/question/'
    for data in inputData:
      x = data["position"]
      print(baseUrl+path+str(x))
      response = requests.get(baseUrl+path+str(data["position"]))
      responseJson = json.loads(response.text)
      # Verify the Response Headers
      assert response.headers['Content-Type'] == "application/json"
      # Verify correct HTTP status code
      assert response.status_code == 200
      # Verify Response Payload data
      assert jsonpath.jsonpath(responseJson,'$.id')[0] == data["id"]
      assert jsonpath.jsonpath(responseJson,'$.position')[0] == data["position"]
      assert jsonpath.jsonpath(responseJson,'$.question')[0] == data["question"]


def test_read_question_invalid_data():
    inputData = {'0','123456','-1'} # Check with invalid numbers as position
    path = '/question/'
    for data in inputData:
        response = requests.get(baseUrl+path+str(data))
        responseJson = json.loads(response.text)

        # Verify correct HTTP status code
        assert response.status_code != 200
         # Verify Response Payload data
        assert jsonpath.jsonpath(responseJson,'$.detail')[0] == "Error"

