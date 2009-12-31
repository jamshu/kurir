'''
Created on Nov 9, 2009

@author: gumuz
'''

DEBUG = True

if __name__ == "__main__":
    if DEBUG:
        # recompile ui
        import popen2
        commands = [r"pyuic4 .\ui\kurir_main.ui > .\ui\kurir_main_window.py",
                    r"pyuic4 .\ui\kurir_accounts.ui > .\ui\kurir_accounts_dialog.py",
                    r"pyuic4 .\ui\kurir_send.ui > .\ui\kurir_send_dialog.py"]
        
        for cmd in commands:
            print popen2.popen2(cmd)[0].read()
        
        
    import sys
    from PyQt4.QtGui import *
    from kurir_main import KurirMainWindow
    
    app = QApplication(sys.argv)
    
    mainwindow = KurirMainWindow()
    mainwindow.show()
    
    
    # command line option to add files
    if sys.argv[1:]:
        mainwindow.add_files(sys.argv[1:])
    
    sys.exit(app.exec_())