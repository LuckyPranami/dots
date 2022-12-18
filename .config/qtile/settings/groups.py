from libqtile.config import Group, ScratchPad, DropDown, Key
from libqtile.config import Key, Group, Match
from libqtile.lazy import lazy
from .keys import mod, keys


groups = [Group(i) for i in "123456789"]
# groups = [Group(i) for i in ["", "", "", "", "ﭮ", "", "", "", "",]]

# groups = [
#     Group(name="1", layout="monadtall", matches=[
#           Match(wm_class=["alacritty"])]),
#     Group(name="2", layout="monadtall",
#           matches=[Match(wm_class=["code"])]),
#     Group(name="3", layout="monadtall", matches=[
#           Match(wm_class=["firefox", "brave"])]),
#     Group(name="4"),
#     Group("5", layout="max", matches=[Match(wm_class=["discord"])]),
#     Group("6", layout="max", matches=[Match(wm_class=["discord"])]),
#     Group("7", layout="max",        matches=[Match(wm_class=[
#           "spotify", "pragha", "clementine", "deadbeef", "audacious"]), Match(title=["VLC media player"])]),
# ]

#     ScratchPad("scratchpad", [
#         # define a drop down terminal.
#         # it is placed in the upper third of screen by default.
#         DropDown("term", "urxvt", opacity=0.8),

#         # define another terminal exclusively for ``qtile shell` at different position
#         DropDown("qtile shell", "urxvt -hold -e 'qtile shell'",
#                  x=0.05, y=0.4, width=0.9, height=0.6, opacity=0.9,
#                  on_focus_lost_hide=True)]),


for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# groups = [Group(i) for i in [
#     "   ", "   ", "   ", "   ", "  ", "   ", "   ", "   ", "   ",
# ]]

# for i, group in enumerate(groups):
#     actual_key = str(i + 1)
#     keys.extend([
#         # Switch to workspace N
#         Key([mod], actual_key, lazy.group[group.name].toscreen()),
#         # Send window to workspace N
#         Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
#     ])


keys = [
    # toggle visibiliy of above defined DropDown named "term"
    Key([], 'F11', lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([], 'F12', lazy.group['scratchpad'].dropdown_toggle('qtile shell')),
]
