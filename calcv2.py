from PyQt5 import QtWidgets , uic , QtGui
import math



def somme():
    a=u.ImpX.text()
    b=u.ImpY.text()
    if a.isnumeric() and (len(a)>0) and b.isnumeric() and (len(b)>0):
        u.res.setText(str(int(a)+int(b)))
    else :
        u.res.setText("ERROR")



def fois():
    a=u.ImpX.text()
    b=u.ImpY.text()
    if a.isnumeric() and (len(a)>0) and b.isnumeric() and (len(b)>0):
        u.res.setText(str(int(a)*int(b)))
    else :
        u.res.setText("ERROR")
        
def moins():
    a=u.ImpX.text()
    b=u.ImpY.text()
    if a.isnumeric() and (len(a)>0) and b.isnumeric() and (len(b)>0):
        u.res.setText(str(int(a)-int(b)))
    else :
        u.res.setText("ERROR")
        
def div():
    a=u.ImpX.text()
    b=u.ImpY.text()
    if a.isnumeric() and (len(a)>0) and b.isnumeric() and (len(b)>0):
        if( int(b) == 0):
            u.res.setText("division par 0!")
            QtWidgets.QMessageBox.critical(u,"ERROR","DIVISION PAR 0 IMPOSSIBLE ",QtWidgets.QMessageBox.Ok)
        else:
            u.res.setText("{:5.2f}".format(int(a)/int(b)))
            
    else :
        u.res.setText("ERROR")
def out():
    u.hide()
    app.quit()
def clear():
    a=u.ImpX.clear()
    b=u.ImpY.clear()
    c =u.res.clear()
'''def PGCD():
    a=u.ImpX.text()
    b=u.ImpY.text()
    '''
    
        
    
    
def PPCM():
    a=u.ImpX.text()
    b=u.ImpY.text()
    if a>=b:
        maxi=a
        mini=b
    

#def base():
    
def init():
    u.base.setChecked(True)
def base():
    u.add.setVisible(True)
    u.fois.setVisible(True)
    u.delt.setVisible(True)
    u.div.setVisible(True)
    u.PGCD.setVisible(False)
    u.PPCM.setVisible(False)
def arr():
    u.add.setVisible(False)
    u.fois.setVisible(False)
    u.delt.setVisible(False)
    u.div.setVisible(False)
    u.PGCD.setVisible(True)
    u.PPCM.setVisible(True)



app = QtWidgets.QApplication([])
app.beep()
u = uic.loadUi('calcv2.ui')
u.show()
u.ImpX.setFocus()
u.add.clicked.connect(somme)
u.fois.clicked.connect(fois)
u.delt.clicked.connect(moins)
u.div.clicked.connect(div)
u.close.clicked.connect(out)
u.reset.clicked.connect(clear)
#u.PGCD.clicked.connect(PGCD)
#u.PPCM.clicked.connect(PPCM)
u.arr.toggled.connect(arr)
u.base.toggled.connect(base)
init()

app.exec_()

