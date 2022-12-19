from libqtile import widget


[widget.Image(
    filename='~/.config/qtile/icons/python.png',
    scale='False',
    margin_x=8,
    mouse_callbacks={
        'Button1': lambda: qtile.cmd_spawn(file_launcher2)}
),
    widget.GroupBox(
    padding=4,
    active=colors[2],
    inactive=colors[1],
    highlight_color=[backgroundColor, workspaceColor],
    highlight_method='line',
),
    widget.Prompt(),
    widget.TextBox(
    text='\u25e2',
    padding=0,
    fontsize=50,
    background=backgroundColor,
    foreground=workspaceColor),
    widget.CurrentLayout(
    scale=0.7,
    background=workspaceColor
),
    widget.TextBox(
    text='\u25e2',
    padding=0,
    fontsize=50,
    background=workspaceColor,
    foreground=backgroundColor
),
    widget.WindowName(
    foreground=colors[5],
),
    widget.Chord(
    chords_colors={
        'launch': (foregroundColor, foregroundColor),
    },
    name_transform=lambda name: name.upper(),
),
    widget.TextBox(
    text='\u25e2',
    padding=0,
    fontsize=50,
    background=backgroundColor,
    foreground=foregroundColorTwo
),
    widget.TextBox(
    text='\u25e2',
    padding=0,
    fontsize=14,
    background=foregroundColorTwo,
    foreground=foregroundColorTwo
),
    widget.Net(
    interface="wlp4s0",
    format=' {down} ↓↑ {up}',
    foreground=colors[7],
    background=foregroundColorTwo,
    padding=8
),
    widget.CPU(
    format='  {freq_current}GHz {load_percent}%',
    background=foregroundColorTwo,
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
        terminal + ' -e htop')},
    foreground=colors[10],
    padding=8
),
    widget.Memory(
    background=foregroundColorTwo,
    foreground=colors[4],
    fmt='  {}',
    padding=8
),
    widget.CheckUpdates(
    update_interval=3600,
    distro="Ubuntu",
    display_format="Updates: {updates} ",
    no_update_string=" No Updates",
    colour_have_updates=colors[9],
    colour_no_updates=colors[5],
    padding=8,
    background=foregroundColorTwo
),
    widget.Volume(
    foreground=colors[8],
    background=foregroundColorTwo,
    fmt=': {}',
    padding=8
),

    widget.Battery(
    charge_char='',
    discharge_char='',
    format='  {percent:2.0%} {char}',
    foreground=colors[6],
    background=foregroundColorTwo,
    padding=8,
),
    widget.TextBox(
    text='\u25e2',
    padding=0,
    fontsize=50,
    background=foregroundColorTwo,
    foreground=backgroundColor
),
    widget.Systray(
    padding=8
),
    widget.Clock(format=' %a, %d. %m. %Y. |  %I:%M %p',
                 foreground=colors[2],
                 background=backgroundColor,
                 padding=8
                 ),
    widget.QuickExit(
    fmt=' ',
    foreground=colors[9],
    padding=8
),
]
