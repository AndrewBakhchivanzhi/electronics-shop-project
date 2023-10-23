"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import csv

item1 = Item("Смартфон", 10000, 20)
def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000

def test_apply_discount():
    Item.pay_rate = 0.75
    item1.apply_discount()
    assert item1.price == 7500

def test_string_to_number():
    assert Item.string_to_number('6') == 6
    assert Item.string_to_number('7.1') == 7
    assert Item.string_to_number('8.9') == 8


def test_instantiate_from_csv():
    Item.instantiate_from_csv('C:\\Users\\Andrew\\PycharmProjects\\electronics-shop-project\\src\\items.csv')
    assert len(Item.all) == 5

def test_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"

def test_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == 'Смартфон'