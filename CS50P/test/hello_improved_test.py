from hello_improved import hello
def test_name():
    assert hello('David') == 'Hello, David'
def test_default():
    assert hello() == 'Hello, World'