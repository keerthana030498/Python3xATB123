import pytest
import requests
import allure


@allure.title("Create a valid booking")
@allure.description("TC01 --- Create a valid booking")
@allure.testcase("TC01")
@pytest.mark.smoke
def test_create_valid_booking():
    # URLs
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path

    # Headers
    headers = {"Content-Type": "application/json"}

    # Payload
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    # Send the POST request
    response = requests.post(url=URL, headers=headers, json=json_payload)

    # Convert the response to JSON
    responseData = response.json()

    # Assertions
    assert response.status_code == 200

    assert "bookingid" in responseData
    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] > 0

    assert "booking" in responseData

    booking = responseData["booking"]

    assert booking["firstname"] == "Jim"
    assert booking["firstname"] is not None
    assert booking["lastname"] == "Brown"
    assert booking["lastname"] is not None
    assert booking["totalprice"] == 111
    assert booking["depositpaid"] == True
    assert booking["additionalneeds"] == "Breakfast"
    assert booking["bookingdates"]["checkin"] == "2018-01-01"
    assert booking["bookingdates"]["checkout"] == "2019-01-01"


@allure.title("Missing required field firstname")
@allure.description("TC01 --- Missing required field firstname")
@allure.testcase("TC02")
@pytest.mark.smoke
def test_missing_firstname():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path

    # Headers
    headers = {"Content-Type": "application/json"}

    # Payload
    json_payload = {
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    # Send the POST request
    response = requests.post(url=URL, headers=headers, json=json_payload)

    # Convert the response to JSON
    #responseData = response.json()

    # Assertions
    assert response.status_code == 500
    print("Response content:", response.text)