import rumps


config = {
    "app_name": "Pomodoro",
    "start_timer": "Start Timer 🏋️",
    "start_break": "Start break 🛀",
    "stop_timer": "Stop Timer",
    "stop_break": "Stop break",
    "interval": 1500,  # 25 min * 60s
    "break_interval": 300,  # 5 min * 60 
    "mode": "🏋️",  # In task mode
    # "mode": "🛀" # In break mode
}


def done_message():
    if config["mode"] == "🏋️":
        return "Well done!! Now let's take a break 😉"

    return "Are you ready for the new challenge 😎"


def set_up_menu():
    time_runner.stop()
    time_runner.count = 0

    timer_button.set_callback(start_timer)
    timer_button.title = config["start_timer"]
    break_button.set_callback(start_break)
    break_button.title = config["start_break"]

    app.title = "🧲"


def app_title(percent=0):
    if percent <= 20:
        return f"🧲 ﹅⁃⁃⁃⁃ {percent}%"
    if percent > 20 and percent <= 40:
        return f"🧲 ﹅﹅⁃⁃⁃ {percent}%"
    if percent > 40 and percent <= 60:
        return f"🧲 ﹅﹅﹅⁃⁃ {percent}%"
    if percent > 60 and percent <= 80:
        return f"🧲 ﹅﹅﹅﹅⁃ {percent}%"
    if percent > 80:
        return f"🧲 ﹅﹅﹅﹅﹅ {percent}%"


def on_tick(sender):
    time_left = sender.end - sender.count
    mins = time_left // 60 if time_left >= 0 else time_left // 60 + 1
    secs = time_left % 60 if time_left >= 0 else (-1 * time_left) % 60
    if time_left < 0:
        rumps.notification(
            title="Time is up!",
            subtitle=done_message(),
            message="",
        )

        set_up_menu()
    else:
        percent = (sender.count * 100)  // sender.end
        app.title = app_title(percent)
    sender.count += 1


def start_timer(sender):
    config["mode"] = "🏋️"
    time_runner.count = 0
    time_runner.end = config["interval"]
    time_runner.start()
    timer_button.title = config["stop_timer"]
    timer_button.set_callback(stop_timer)


def stop_timer(sender):
    print(sender.title)
    set_up_menu()


def start_break(sender):
    config["mode"] = "🛀"
    time_runner.count = 0
    time_runner.end = config["break_interval"]
    time_runner.start()
    break_button.title = config["stop_break"]
    break_button.set_callback(stop_timer)


def duration_time_label():
    return f"Task: {config['interval'] // 60} min"


def pop_duration_time(sender):
    response = rumps.Window("Please enter a new duration (minutes)").run()
    if response.clicked:
        duration_interval = config["interval"] // 60
        try:
            duration_interval = int(response.text)
        finally:
            config["interval"] = duration_interval * 60
            sender.title = duration_time_label()


def break_time_label():
    return f"Break: {config['break_interval'] // 60} min"


def pop_break_time(sender):
    response = rumps.Window("Please enter a new break period (minutes)").run()

    break_interval = config["break_interval"] // 60
    if response.clicked:
        try:
            break_interval = int(response.text)
        finally:
            config["break_interval"] = break_interval * 60
            sender.title = break_time_label()


def about(sender):
    rumps.alert("Made by Quang Son with ❤️")


app = rumps.App(config["app_name"])
time_runner = rumps.Timer(on_tick, 1)

timer_button = rumps.MenuItem(title=config["start_timer"], callback=start_timer)
change_duration_menu = rumps.MenuItem(
    title=duration_time_label(), callback=pop_duration_time
)

break_button = rumps.MenuItem(title=config["start_break"], callback=start_break)
change_break_menu = rumps.MenuItem(title=break_time_label(), callback=pop_break_time)

about_button = rumps.MenuItem(title="About", callback=about)

blank_one = rumps.MenuItem(title="⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻", callback=None)
blank_two = rumps.MenuItem(title="⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻", callback=None)

app.menu = [
    change_duration_menu,
    timer_button,
    blank_one,
    change_break_menu,
    break_button,
    blank_two,
    about_button,
]


if __name__ == "__main__":
    set_up_menu()
    app.run()
