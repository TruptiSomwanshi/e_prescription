import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyDqoRHH1cbTWLUYRlH1vP5R-zrkCCAT0MI",
  'authDomain': "e-prescription-ff041.firebaseapp.com",
  'projectId': "e-prescription-ff041",
  'storageBucket': "e-prescription-ff041.appspot.com",
  'messagingSenderId': "437020753136",
  'appId': "1:437020753136:web:c2c432dd239a9debfe1635",
  'databaseURL':''
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def login(email,password):
    result = ''
    try:
        login = auth.sign_in_with_email_and_password(email,password)
        result = 'success'
    except :
        result = 'unsuccess'
    return result

def signUp(mail,passW):
        result = ''
        try:
            login = auth.create_user_with_email_and_password(mail,passW)
            result ='success'
        except :
            result = 'unsuccess'
        return result