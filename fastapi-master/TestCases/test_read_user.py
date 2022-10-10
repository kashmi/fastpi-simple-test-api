import json
import requests

baseUrl = 'http://127.0.0.1:8000'

def test_read_user():
    path = '/user'
    response = requests.get(baseUrl+path)
    responseJson = json.loads(response.text)
    name = [people['name'] for people in responseJson]
    id = [people['id'] for people in responseJson]
    mail = [people['mail'] for people in responseJson]
    phone = [people['phone'] for people in responseJson]
    # Verify correct HTTP status code
    assert response.status_code == 200

    # Verify the Response Headers
    assert response.headers['Content-Type'] == "application/json"

    # Verify the Response Headers
    assert response.headers['Content-Length'] == "153"

    # Verify response payload.
    if (len(responseJson) or len(name) or len(id) or len(mail) or len(phone)) == 0:
        print("Some or All the Keys doesnot have a valid value", (len(name) or len(id)))
        assert False
    else:
        print("All the key having values",flush=True)
        assert True