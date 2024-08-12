import allure
import pytest

@allure.title("tc01 , verifiying the addition")
@allure.description("sum of 2")
@pytest.mark.smoke
def test_addition():
    assert 1+1 == 2