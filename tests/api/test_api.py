import pytest
import requests


@pytest.mark.api
def test_api_retorna_sucesso():
    resposta = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert resposta.status_code == 200
    assert resposta.json()["id"] == 1