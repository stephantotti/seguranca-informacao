import pyrebase
import os
import stat
from datetime import datetime

def registrar_acesso(user):

    if os.path.isfile("acesso.txt"):
        os.chmod("acesso.txt", stat.S_IRWXU)
        print("Arquivo existe")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        file = open("acesso.txt", "a")
        file.write("\n")
        file.write(str(user) + "-" + dt_string)
        file.close()
        os.chmod("acesso.txt", stat.S_IRUSR)


    else:
        file = open("acesso.txt",'w')
        file.close()
        print("Arquivo criado")
        os.chmod("acesso.txt", stat.S_IRUSR)



firebaseConfig = {
    "apiKey": "AIzaSyCPZOV3lGg0MPwU-pD6Tx1xOkrRUReUJmU",
    "authDomain": "fir-pucpr-62938.firebaseapp.com",
    "projectId": "fir-pucpr-62938",
    "databaseURL": "https://" + "fir-pucpr" + ".firebaseio.com",
    "storageBucket": "fir-pucpr-62938.appspot.com",
    "messagingSenderId": "632394532514",
    "appId": "1:632394532514:web:829388b8d8c4a75f85f9fb",
    "measurementId": "G-WB93NWBWZ1"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

resposta_u = input("Usuario novo ? (s/n) ")

if resposta_u == "s":
    user = input("Digite seu e-mail: ")
    password = input("Digite sua senha, com pelo menos 6 caracteres: ")
    status = auth.create_user_with_email_and_password(user, password)
    auth.send_email_verification(status["idToken"])

elif resposta_u == "n":

    user = input("Digite seu e-mail: ")
    password = input("Digite sua senha, com pelo menos 6 caracteres: ")
    #status = auth.create_user_with_email_and_password(user,password)
    try:
        status= auth.sign_in_with_email_and_password(user,password)
        idToken = status["idToken"]
        print("Resultado: ", status)
        print("Token", idToken)
        info = auth.get_account_info(idToken)
        print("Info: ", info)
        email_chek = info["users"]
        verifyEmail= email_chek[0]["emailVerified"]

        if verifyEmail:
            print("Email verificado")
            print(os.getcwd())
            registrar_acesso(user)
        else:
            print("Email nao verificado")
            auth.send_email_verification(status["idToken"])
    except:
        print("login/senha invalidos")
else:
    print("Opcao invalida")