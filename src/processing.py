from typing import List, Dict

def filter_by_state(operations: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список операций по значению ключа 'state'.

    :param operations: Список словарей с данными о банковских операциях.
    :param state: Значение фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список операций.
    """
    return [operation for operation in operations if operation.get('state') == state]


def sort_by_date(operations: List[Dict], ascending: bool = False) -> List[Dict]:
    """
    Сортирует список операций по дате.

    :param operations: Список словарей с данными о банковских операциях.
    :param ascending: Порядок сортировки (True — возрастание, False — убывание).
    :return: Отсортированный список операций.
    """
    return sorted(
        operations,
        key=lambda x: x.get('date', ''),
        reverse=not ascending
    )