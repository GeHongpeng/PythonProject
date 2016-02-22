from urllib.request import urlopen

conn = urlopen("http://localhost:8080/cgi-bin/cgi101.py?user=Sue+Smith")
reply = conn.read()
reply
