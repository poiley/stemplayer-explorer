import sys
from ui import app, main_window
        
def main():
    ui = main_window()
    ui.show()

    app.exec_()

if __name__ == '__main__':
    main()
