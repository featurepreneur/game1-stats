from flask import Flask
from faker import Faker
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["3 per day"]
)

@app.route("/name",methods=["GET","POST"])
def startpy():
    
    random_name_list = generate_random_names() 
    result={}
    result.update({"name":random_name_list})
    return result
    #return random_name_list
    
    
def generate_random_names():
    fake=Faker()
    random_names = []
    for x in range(5) :
        random_names.append(fake.name())
    return  random_names  
    

@app.route("/address",methods=["GET","POST"])
def startpy1():
    
    random_address_list = generate_random_address()
    result={}
    result.update({"address":random_address_list})
    return result
    #return random_name_list
    
    
def generate_random_address():
    fake=Faker()
    random_address = []
    for x in range(5) :
        random_address.append(fake.address())
    return  random_address
    



@app.route("/email",methods=["GET","POST"])
def startpy2():
    
    random_email_list = generate_random_email() 
    result={}
    result.update({"email":random_email_list})
    return result
    #return random_name_list
    
    
def generate_random_email():
    fake=Faker()
    random_email = []
    for x in range(5) :
        random_email.append(fake.email())
    return  random_email
    


if __name__ =="__main__":
    
    app.run(debug=True)
    
