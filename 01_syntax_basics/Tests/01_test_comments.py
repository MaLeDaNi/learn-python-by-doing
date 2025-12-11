def test_comments():
    with open("../Tasks/001_task_comments.py", encoding='utf-8') as f:
        text = f.read()

    lines = text.split('\n')
    single = sum(1 for line in lines if line.strip().startswith('#'))
    assert single >= 2, f"Нужно 2 однострочных комментария!"

    multi = sum(1 for line in lines if line.strip().startswith(("'''", '"""')))
    assert multi >= 6, f"Нужно 2 многострочных комментария!"

    print("Проверка пройдена! Всё хорошо!")