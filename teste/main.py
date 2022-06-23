#importar o pyrebase4 no pip
import pyrebase
import random
import mail_send

def gerador_random():
    codigo= random.randint(100000, 999999)
    return codigo


def otp_checker(otp):
    otp_informada = input("Informe o codigo de acesso unico: ")
    #print(otp)
    if str(otp) == str(otp_informada):
        print("Sucesso")
    else:
        print("Falha")


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

elif resposta_u == "n":

    user = input("Digite seu e-mail: ")
    password = input("Digite sua senha, com pelo menos 6 caracteres: ")
    #status = auth.create_user_with_email_and_password(user,password)
    try:
        status= auth.sign_in_with_email_and_password(user,password)
        idToken = status["idToken"]
        print("Resultado: ", status)
        print("Token", idToken)
        otp = gerador_random()
        #print(otp)
        mail_send.conectar_email(user, otp)
        otp_checker(otp)

    except:
        print("login/senha invalidos")
else:
    print("Opcao invalida")


