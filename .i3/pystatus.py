from i3pystatus import Status

status = Status(standalone=True)

status.register("uname",
    hints = {"markup": "pango"},
    format = "<span font_family='icon' color='#BFA571' size='12800'>\uE80B</span>"+\
             "<span color='#808080'>{release}</span>",)

status.register("clock",
    hints = {"markup": "pango"},
    format = "<span font_family='icon' color='#BFA571' size='12800'>\uE80D</span>"+\
             "<span color='#808080'> %H:%M</span>",)

status.register("clock",
    hints = {"markup": "pango"},
    format = "<span font_family='icon' color='#BFA571' size='12800'>\uE806</span>"+\
             "<span color='#808080'> %a %d %b</span>",)

status.register("weather",
    units="metric",
    location_code="UPXX0049",
#    on_leftclick = ["exec surf 'http://goo.gl/c4GYjL'"],
#    colorize=True,
    hints = {"markup": "pango"},
    format = "<span font_family='icon' color='#BFA571' size='12800'>\uE80A</span>"+\
             "<span color='#808080'> {current_temp} </span>"+\
             "<span font_family='icon' color='#BFA571' size='12800'>\uE808</span>"+\
             "<span color='#808080'> {humidity}% </span>"+\
             "<span font_family='icon' color='#BFA571' size='12800'>\uE809</span>"+\
             "<span color='#808080'> {current_wind}</span>",)

#status.register("runwatch",
#    name="DHCP",
#    path="/var/run/dhclient*.pid",)

status.register("network",
    interface="eth0",
    hints   = {"markup": "pango"},
    format_up ="<span font_family='icon' color='#BFA571' size='12800'>\U0001F5A7</span>"+\
               "<span color='#808080'> {v4cidr}</span>",
    format_down = "",)

status.register("network",
    interface = "eth0",
    hints = {"markup": "pango"},
    format_up = "<span font_family='icon' color='#BFA571' size='12800'>\uE804</span>"+\
                "<span color='#808080'>{bytes_recv:6.0f}K </span>"+\
                "<span font_family='icon' color='#BFA571' size='12800'>\uE803</span>"+\
                "<span color='#808080'>{bytes_sent:5.0f}K</span>",
    format_down = "",
#    dynamic_color = True,
#    start_color = "#00FF00",
#    end_color = "#FF0000",
#    color_down = "#FF0000",
#    upper_limit = 800.0,
    )

#status.register("cpu_usage_bar",
#     format="\U0001F4BB {usage_bar}",)

status.register("cpu_usage_graph",
    graph_width = 6,
    hints = {"markup": "pango"},
    format = "<span font_family='icon' color='#BFA571' size='12800'>\uE807</span>"+\
             "<span color='#808080'>{cpu_graph}</span>",)

status.register("mem_bar",
    hints = {"markup": "pango"},
    format = "<span font_family='icon' color='#BFA571' size='12800'>\uE80C</span>"+\
             "<span color='#808080'>{used_mem_bar}</span>",)

status.register("pulseaudio",
    hints = {"markup": "pango"},
    format = "<span font_family='icon' color='#BFA571' size='12800'>\uE805</span>"+\
             "<span color='#808080'>{volume}%</span>",)

status.register("mpd",
    hints = {"markup": "pango"},
    format="<span color='#808080'>{status} {title}\[{song_elapsed}/{song_length}\]</span>",
    max_field_len=55,
    status={
        "pause": "<span font_family='icon' color='#BFA571' size='12800'>\uE801</span>",
        "play":  "<span font_family='icon' color='#BFA571' size='12800'>\uE800</span>",
        "stop":  "<span font_family='icon' color='#BFA571' size='12800'>\uE802</span>",
    },)

status.run()
