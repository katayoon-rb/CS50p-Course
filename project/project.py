import random
import string

def main():
    todos = []
    actions = ['Add', 'Remove', 'Edit', 'Print', 'Quit']

    while True:
        print('\n' + ', '.join(actions))
        action = input('What do you want to do? ').lower().capitalize()
        while action not in actions:
            action = input('Not a valid action. Try again: ').lower().capitalize()


        if (action != 'Add'):
            if len(todos) == 0:
                print( 'Your todo list is empty,' )
                add( todos, input('Try adding first: ') )


        if (action == 'Add'):
            add( todos, input('Enter what you want to do: ') )

        if (action == 'Remove'):
            remove( todos, get_index(todos) )

        if (action == 'Edit'):
            index = get_index(todos)
            changed = input('The new value: ')
            edit( todos, index, changed )

        if (action == 'Print'):
            print( printAct(todos) )

        if (action == 'Quit'):
            print( printAct(todos) )
            break



def get_index(todos):
    i = 1
    for item in todos:
        print(str(i) + ' ' + item)
        i += 1

    index = input('which one (enter a number)? ')
    try:
        index = int(index) - 1
    except ValueError:
        index = int(input('Enter a number: ')) - 1

    return index



def add(todos, task):
    todos.append(task)
    return todos


def remove(todos, idx):
    todos.pop(idx)
    return todos


def edit(todos, idx, new):
    todos[idx] = new
    return todos


def printAct(todos):
    i = 0
    output = ''
    for item in todos:
        i += 1
        output += str(i) + ' - ' + item + '\n'
    return output



if __name__ == "__main__":
    main()import random
import string

def main():
    todos = []
    actions = ['Add', 'Remove', 'Edit', 'Print', 'Quit']

    while True:
        print('\n' + ', '.join(actions))
        action = input('What do you want to do? ').lower().capitalize()
        while action not in actions:
            action = input('Not a valid action. Try again: ').lower().capitalize()


        if (action != 'Add'):
            if len(todos) == 0:
                print( 'Your todo list is empty,' )
                add( todos, input('Try adding first: ') )


        if (action == 'Add'):
            add( todos, input('Enter what you want to do: ') )

        if (action == 'Remove'):
            remove( todos, get_index(todos) )

        if (action == 'Edit'):
            index = get_index(todos)
            changed = input('The new value: ')
            edit( todos, index, changed )

        if (action == 'Print'):
            print( printAct(todos) )

        if (action == 'Quit'):
            print( printAct(todos) )
            break



def get_index(todos):
    i = 1
    for item in todos:
        print(str(i) + ' ' + item)
        i += 1

    index = input('which one (enter a number)? ')
    try:
        index = int(index) - 1
    except ValueError:
        index = int(input('Enter a number: ')) - 1

    return index



def add(todos, task):
    todos.append(task)
    return todos


def remove(todos, idx):
    todos.pop(idx)
    return todos


def edit(todos, idx, new):
    todos[idx] = new
    return todos


def printAct(todos):
    i = 0
    output = ''
    for item in todos:
        i += 1
        output += str(i) + ' - ' + item + '\n'
    return output



if __name__ == "__main__":
    main()