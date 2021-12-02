def StripeInputs():
    html = open("./clone/index.html", "r").read()
    from bs4 import BeautifulSoup as bs
    sp = bs(html, "html.parser")

    inputs = sp.find_all("input")

    # email
    email_input = ""
    for i in inputs:
        if i["type"] == "text" or i["type"] == "email":
            if i["name"] == "email" or  i["name"] != "":
                email_input = i["name"]

    password_input = ""
    for i in inputs:
        if i["type"] == "password":
            password_input =  i["name"]

    return {"email":email_input, "pwd":password_input}
