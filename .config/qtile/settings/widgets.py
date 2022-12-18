from libqtile import widget

colors = [["#2e3440", "#2e3440"],  # color 0  dark grayish blue
          ["#2e3440", "#2e3440"],  # color 1  dark grayish blue
          ["#3b4252", "#3b4252"],  # color 2  very dark grayish blue
          ["#434c5e", "#434c5e"],  # color 3  very dark grayish blue
          ["#4c566a", "#4c566a"],  # color 4  very dark grayish blue
          ["#d8dee9", "#d8dee9"],  # color 5  grayish blue
          ["#e5e9f0", "#e5e9f0"],  # color 6  light grayish blue
          ["#eceff4", "#eceff4"],  # color 7  light grayish blue
          ["#8fbcbb", "#8fbcbb"],  # color 8  grayish cyan
          ["#88c0d0", "#88c0d0"],  # color 9  desaturated cyan
          ["#81a1c1", "#81a1c1"],  # color 10 desaturated blue
          ["#5e81ac", "#5e81ac"],  # color 11 dark moderate blue
          ["#bf616a", "#bf616a"],  # color 12 slightly desaturated red
          ["#d08770", "#d08770"],  # color 13 desaturated red
          ["#ebcb8b", "#ebcb8b"],  # color 14 soft orange
          ["#a3be8c", "#a3be8c"],  # color 15 desaturated green
          ["#b48ead", "#b48ead"]]  # color 16 grayish magenta


primary_widgets = [
    widget.CurrentLayout(),
    widget.GroupBox(),
    widget.Prompt(),
    widget.WindowName(),
    widget.Chord(
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
    # widget.StatusNotifier(),
    widget.Battery(format='{percent:2.0%}'),
    widget.Volume(),
    widget.Backlight(
        # brightnes_file='/sys/class/backlight/intel_backlight/brightness',
        backlight_name='intel_backlight',
        # change_command="brightnessctl --device='intel_backlight' set {0}",
        # step=
        # format='{percent:2.0%}',
        # background=colors[6],
        # foreground=colors[1],
    ),
    widget.Systray(),
    widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
    widget.QuickExit(
        fontsize=22,
        default_text='\uf011',
        countdown_format='{}'
    ),
    widget.Spacer(length=15)

]

widget_defaults = dict(
    font="Cascadia Code",
    fontsize=14,
    padding=2,
)
extension_defaults = widget_defaults.copy()
