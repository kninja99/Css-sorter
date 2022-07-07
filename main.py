from os import kill
from CSS_Sorter import sortCss

def main():
    print('Enter the path of the css file you wish to sort')
    print('* note if the path is in the projects root directory you can just input the fileName.css *')
    print('command to exit the program: *')
    user_input = input('Path: ')
    if user_input == '*':
        print('terminated')
    else:
        try:
            sortCss(user_input)
        except:
            print('invalid path, try again')
            main()
            
if __name__ == '__main__':
    main()