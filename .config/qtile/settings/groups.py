from libqtile.config import Group, ScratchPad, DropDown, Key, Match
from libqtile.lazy import lazy
from .keys import mod, keys


groups = [
    Group("TERM", layout='monadtall', matches=[Match(wm_class=["Alacritty"])]),
    Group("WWW", layout='monadtall', matches=[
          Match(wm_class=["brave-browser", "chromium", "firefox"])]),
    Group("DEV", layout='monadtall', matches=[Match(wm_class=["code"])]),
    Group("DOC", layout='monadtall'),
    Group("CHAT", layout='monadtall', matches=[Match(wm_class=["discord"])]),
    Group("MUS", layout='max', matches=[Match(wm_class=["spotify"])]),
    Group("VID", layout='max', matches=[
          Match(title=["VLC media player"])]),
    Group("SYS", layout='monadtall'),
    # Group("VBOX", layout='monadtall'),
    # Group("GFX", layout='floating')
]

groups.append(ScratchPad('scratchpad', [
    DropDown('terminal', "alacritty", width=0.6, height=0.6,
             x=0.2, y=0.2, opacity=.5),
    DropDown('htop', "alacritty -e htop", width=0.9, height=0.9,
             x=0.05, y=0.05, opacity=.5)
]))

keys.extend([
    Key([mod], "Down", lazy.group['scratchpad'].dropdown_toggle('terminal')),
    Key([mod], "Up", lazy.group['scratchpad'].dropdown_toggle('htop')),
    #     Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('text_editor')),
])
