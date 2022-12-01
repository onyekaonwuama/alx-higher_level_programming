#!/usr/bin/python3

if __name__ == "__main__":
    """print all names not starting with __ using hidden 4 module"""
    import hidden_4

    names = dir(hidden_4)
    for i in names:
        if i[:2] != "__":
            print(i)
    
