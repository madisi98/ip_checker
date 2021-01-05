import os
import urllib.request
import pushsafer

def send_notification(external_ip):
    pkey = open(os.path.expanduser('~/.pushsafer')).readline().strip()
    pushsafer.init(pkey)
    c = pushsafer.Client('')
    c.send_message(external_ip, 'NEW IP', 'a', '1', '', '', '', '', '', '0', '', '', '0', '', '', '')

def launcher():
    root_path = os.path.abspath(os.path.dirname(__file__))
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    saved_ip = open(os.path.join(root_path, 'ip')).readline().strip()
    if external_ip != saved_ip:
        open(os.path.join(root_path, 'ip'), 'w').write(str(external_ip))
        send_notification(external_ip)
        
