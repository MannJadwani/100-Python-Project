from datetime import datetime

end_time = datetime(2023,10,28,13)

sites_to_block = ['www.facebook.com']

hosts_path = "/etc/hosts"

redirect = "127.0.0.1"

def block_sites():
    if datetime.now() < end_time:
        print("block sites")
        with open(hosts_path, 'r+') as hosts:
            host_content = hosts.read()
            for sites in sites_to_block:
                if sites not in host_content:
                    hosts.write(redirect+ " "+sites+"\n")
    else:
        print("unblock sites")
        with open(hosts_path, 'r+') as hosts:
            lines = hosts.readlines()
            hosts.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hosts.write(line)
            hosts.truncate()
    
if __name__ == "__main__":
        block_sites()



