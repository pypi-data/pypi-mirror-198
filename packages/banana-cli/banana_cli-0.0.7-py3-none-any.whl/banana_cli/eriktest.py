from process.trigger import trigger

def memdump():
    for i in globals():
        print(i)

def main():

    # trigger("import sys")
    # trigger("sys.path.append('./venv/lib/python3.10/site-packages')")

    trigger("import bs4")

    # trigger("x = 5")

    # trigger("print(x)")


if __name__ == "__main__":
    main()