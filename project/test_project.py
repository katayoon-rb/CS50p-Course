import project

def main():
    test_add()
    test_remove()
    test_edit()
    test_printAct()



def test_add():
    assert project.add([], 'first') == ['first']
    assert project.add(['first'], 'second') == ['first', 'second']


def test_remove():
    assert project.remove(['first'], 0) == []
    assert project.remove(['first', 'second'], 0) == ['second']
    assert project.remove(['first', 'second', 'third', 'fourth'], 2) == ['first', 'second', 'fourth']


def test_edit():
    assert project.edit(['first'], 0, 'new') == ['new']
    assert project.edit(['first', 'second'], 0, 'new') == ['new', 'second']
    assert project.edit(['first', 'second', 'third', 'fourth'], 2, 'new') == ['first', 'second', 'new', 'fourth']


def test_printAct():
    assert project.printAct(['first']) == '1 - first\n'
    assert project.printAct(['first', 'second']) == '1 - first\n2 - second\n'
    assert project.printAct(['first', 'second', 'third', 'fourth']) == '1 - first\n2 - second\n3 - third\n4 - fourth\n'




if __name__ == "__main__":
    main()