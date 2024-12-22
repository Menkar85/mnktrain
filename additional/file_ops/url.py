import urllib.request


def url_open(url):
    lst = list()
    try:
        with urllib.request.urlopen(url) as webpage:
            for line in webpage:
                line = line.decode('utf-8')
                line = line.strip()
                lst.append(line)
                stng = '\n'.join(lst)
        return stng
    except Exception as e:
        print(e)


if __name__ == "__main__":
    s = "http://dfedorov.spb.ru/python3/src/romeo.txt"
    print(url_open(s))
