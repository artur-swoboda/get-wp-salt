import urllib.request

def get_wp_salt():
    salts = []
    contents = urllib.request.urlopen(
        "https://api.wordpress.org/secret-key/1.1/salt/").read().decode('utf-8')

    for line in contents.splitlines():
        salts.append(line.split("'")[3])

    print(salts)

get_wp_salt()
