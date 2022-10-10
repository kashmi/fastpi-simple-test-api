import json
import jsonpath
import requests
# import app.api.api

baseUrl = 'http://127.0.0.1:8000'

def test_read_alternatives():
    with open('data/alternatives.json') as stream:
        inputData = json.load(stream)
    path = '/alternatives/'
    for data in inputData:
      print(baseUrl+path+str(data["question_id"]))
      response = requests.get(baseUrl+path+str(data["question_id"]))
      responseJson = json.loads(response.text)
      # Verify correct HTTP status code
      assert response.status_code == 200

      # Verify the Response Headers
      assert response.headers['Content-Type'] == "application/json"

      for x in responseJson:
        # Verify response payload.
        assert jsonpath.jsonpath(x,'$.question_id')[0] == data["question_id"]



