# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля
from typing import List, Union

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def read_csv(csv: str) -> List[List[str]]:
    return [row.split(';') for row in csv.split('\n')]


def _sort_by_age(data: List[List[str]]) -> List[List[Union[str, int]]]:
    return sorted(data, key=lambda x: int(x[1]))


def _filter_by_age(data: List[List[str]], age=10) -> List[List[Union[str, int]]]:
    return [row for row in data if int(row[1]) >= age]


def get_users_list(csv: str) -> List[List[Union[str, int]]]:
    data = read_csv(csv)
    data = _sort_by_age(data)
    data = _filter_by_age(data)
    return data


if __name__ == '__main__':
    print(get_users_list(csv))
