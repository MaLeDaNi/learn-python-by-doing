
import os
import sys


def test_variables():
    """Проверяем переменные в файле пользователя"""

    task_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'Tasks',
        'task_01.py'
    )

    task_path = os.path.abspath(task_path)

    if not os.path.exists(task_path):
        raise FileNotFoundError(f"Файл не найден: {task_path}")

    with open(task_path, 'r', encoding='utf-8') as f:
        user_code = f.read()

    namespace = {}

    try:
        exec(user_code, {}, namespace)
    except Exception as e:
        assert False, f"Ошибка в вашем коде: {e}"


    assert 'number' in namespace, "Создайте переменную с именем 'number'"
    assert namespace['number'] == 1024, f"Переменная 'number' должна равняться 1024, а у вас: {namespace['number']}"

    assert 'name' in namespace, "Создайте переменную 'name'"
    assert namespace['name'] == 'Alex', f"'name' должна быть 'Alex', а у вас: {namespace['name']}"

    assert 'minimal_age' in namespace, "Создайте переменную 'minimal_age'"
    assert namespace['minimal_age'] == None, f"'minimal_age' должна быть 'None', а у вас: {namespace['minimal age']}"

    print("Всё отлтчно!")