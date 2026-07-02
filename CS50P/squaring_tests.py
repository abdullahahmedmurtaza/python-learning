import pytest;
from squaring import square

def main():
    test_square()

# def test_square():
#     if(square(2)!=4):
#         print('2 squared was not 4')
#     if(square(3)!=9):
#         print('3 squared was not 9')
#     if(square(4)!=16):
#         print('2 squared was not 16')
        
# for more and more test cases the if statements are not suitable. That is why we have to use another keyword called 'assert' --> boldly claims something is true, if it is true nothing happens. Otherwise an AssertionError is thrown. 

# assert is not that user-friendly but for developers it is good because it the code is short and it gives an exact line number for the dev to trace back.

# To make it more user-friendly, we can wrap every assert in a try block and catch the AssertionError. But it increases the code.

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(4) == 16
#     assert square(5) == 25
#     assert square(6) == 36
#     assert square(7) == 49
#     assert square(8) == 64
#     assert square(9) == 81




# To solve the problem of the code being much more bulky than the original source code, we use tools like pytest --> a program that automates certain best practices, so that we do not have to implement everything ourselves.We can also use lists and loops

# We can use docs.pytest.org

# Keep each test in a separate function grouped by types.

def test_square_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(5) == 25
    assert square(6) == 36
    assert square(7) == 49
    assert square(8) == 64
    assert square(9) == 81



def test_square_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16
    assert square(-5) == 25
    assert square(-6) == 36
    assert square(-7) == 49
    assert square(-8) == 64
    assert square(-9) == 81
def test_square_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square('cat')

# pytest has a built-in method called pytest.raises(TypeError) that raises an error when a code does not work as expected.  


if(__name__ == '__main__'):
    main()