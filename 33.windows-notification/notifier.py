##Windows 

# from winotify import Notification,audio

# toast = Notification(app_id="Notifier App",
#                      title="Subscribe to Mann Jadwani",
#                      msg="You Must in any case Subscribe to Mann Jadwani",
#                      duration="short")

# toast.show()

##Mac


from mac_notifications import client

if __name__ == "__main__":
    client.create_notification(
        title="Meeting starts now!",
        subtitle="Team Standup",
        icon="/Users/jorrick/zoom.png",
        action_button_str="Join zoom meeting",
    )