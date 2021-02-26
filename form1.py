from PyQt5 import QtWidgets,uic
import webbrowser
#Bouton valider
def valid() :
    global call_2
    f=open('F_eleve.txt','a+')
    nom=call.np.text()
    prénom=call.npr.text()
    numéro=call.num.text()
    numéro_de_téléphone=call.tlf.text()
    age=call.age.text()
    adresse=call.addd.text()
    x=f'Nom : {nom}\nPrénom : {prénom}\nNuméro : {numéro}\nNuméro de téléphone : {numéro_de_téléphone}\nAge : {age}\n'

    f.write(x)


    f.close()
    call_2.show()
    x=f'Nom : {nom}\nPrénom : {prénom}\nNuméro : {numéro}\nNuméro de téléphone : {numéro_de_téléphone}\nAge : {age}\n'
    call_2.complete.setText(x)
    
def quit_2():
    app.quit()

#Boutton annuler
def canceling():
    app.quit()
def choix():    
    choix=call.choi.text()
    if choix=="non":
        app.quit()
    if choix=="oui":
        webbrowser.open_new(r'form1.py')
#Program principal
app=QtWidgets.QApplication([])
call=uic.loadUi("form.ui")
call_2=uic.loadUi("okform.ui")
call.pushButton.clicked.connect(valid)
call.pushButton_2.clicked.connect(canceling)
call_2.ok1.clicked.connect(choix)
call.show()
app.exec()
