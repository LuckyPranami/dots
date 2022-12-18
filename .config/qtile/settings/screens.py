from libqtile.config import Screen
from libqtile import bar
from .widgets import primary_widgets


screens = [
    Screen(
        top=bar.Bar(
            primary_widgets,
            24,
            # border_width=[10, 10, 10, 10],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            # border_color=["00000000", "00000000", "00000000", "00000000"],
            # background="#00000000",
            # margin = 5,
        ),
    ),
]


# xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

# command = subprocess.run(
#     xrandr,
#     shell=True,
#     stdout = subprocess.PIPE,
#     stderr = subprocess.PIPE,
# )

# if command.returncode != 0:
#     error=command.stderr.decode("UTF-8")
#     logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
#     connected_monitors=1
# else:
#     connected_monitors=int(command.stdout.decode("UTF-8"))

# if connected_monitors > 1:
#     for _ in range(1, connected_monitors):
#         screens.append(Screen(top=status_bar(secondary_widgets)))
