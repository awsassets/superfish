# How to install
#### Linux and Termux:
- Clone Rp: `git clone https://github.com/J4c5/superfish.git`
- Install the dependencies: `pip3 install -r requirements.txt`

# Arguments and Usage
#### the list of arguments are these:
```sh
--import-template
--local-template
--webserver-port
--webserver-host
--redirect
--output
```
#### description of each argument
- `--import-template`: import a login template using a url for example: `--import-template=https://facebook.com/login`
- `--local-template`: use a local template that you might have downloaded to an index.html, example: `--local-template=./mytemplate/index.html`
- `--webserver-port`: configure a port for the server the default is 8080, example: `--webserver-port=8082`
- `--webserver-host`: configure a host, the default is: 127.0.0 1, example: `--webserver-host=0.0.0.0`
-  `--redirect`: configure where the victim will be directed to post the phishing, example: `--redirect=https://facebook.com`
-  `--output`: edit the phishing output, if you want in csv use: `--output=csv` or you want text: `--output=text`
