from datetime import datetime as dt

hostpath = "/private/etc/hosts"

# loaclhost (will redirect to this host)
redirect = "127.0.0.1"

websitelist = [
    "www.reddit.com",
    "www.facebook.com",
    "www.instagram.com",
    "www.youtube.com",
    "www.cnn.com",
    "www.twitter.com",
    "www.buzzfeed.com",
    "www.yahoo.com",
    "www.tumblr.com",
    "www.netflix.com",
]

blocktime = {
    "start": dt(dt.now().year, dt.now().month, dt.now().day, 9),
    "end": dt(dt.now().year, dt.now().month, dt.now().day, 17)
}

if blocktime["start"] < dt.now() < blocktime["end"]:
    # to know our current mode
    print("Time to focus ...")

    # read the `host` file to check the list
    with open(hostpath, "r+") as file:
        content = file.read()
        for website in websitelist:
            # if your website is not in the `host` file, add the website
            if not website in content:
                with open(hostpath, "a") as writefile:
                    writefile.write(redirect + " " + website + "\n")
else:
    print("Enjoy your free time ...")

    # If the current time is not between working time, remove the websites
    with open(hostpath, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websitelist):
                file.write(line)
        # removing websites from the `host` file
        file.truncate()
