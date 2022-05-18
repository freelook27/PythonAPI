import pytest
import requests

class TestFirstApi:
    names = [
        ("Vitalii"),
        ("Arseniy"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call2(self, name):
            url = 'http://playground.learnqa.ru/api/hello'
            data = {'name': name}

            response = requests.get(url, params=data)
            
            assert response.status_code == 200, "Wrong response code"

            response_dict = response.json()
            assert "answer" in response_dict, "There is no field 'answer' in response"

            if len(name) == 0:
                expected_respose_text = "Hello, someone"
            else:
                expected_respose_text = f"Hello, {name}"

            #expected_respose_text = f"Hello, {name}"
            actual_response_text = response_dict["answer"]
            assert actual_response_text == expected_respose_text, "Actual text in the response is not correct"