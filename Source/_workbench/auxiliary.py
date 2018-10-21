#auxiliary
class log():
    def logging_init():
        open("setupper.log", "w")

    def logging(line):
        import time
        import datetime
        with open("setupper.log", "a") as file:
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            line = str("[" + st + ": " + line + " ]\n")
            file.write(line)