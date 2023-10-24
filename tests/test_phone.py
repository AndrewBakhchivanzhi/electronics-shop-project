import pytest

from src.phone import Phone

def test_add():
    phone1 = Phone("Смартфон", 10000, 20, 2)
    phone2 = Phone("СуперСмартфон", 20000, 15, 1)
    assert phone1 + phone2 == 35

def test_number_of_sim_setter():
    phone = Phone("Смартфон", 10000, 20, 2)
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1
    with pytest.raises(ValueError) as excinfo:
        phone.number_of_sim = 0
    assert "Количество физических SIM-карт должно быть целым числом больше нуля." in str(excinfo.value)



