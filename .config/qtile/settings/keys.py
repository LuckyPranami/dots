from libqtile.config import Key
from libqtile.command import lazy
from libqtile.utils import guess_terminal


# terminal = guess_terminal()
mod = "mod4"
terminal = "alacritty"
browser = "brave"
file_manager = "thunar"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),



    # My Own Keybindings
    # My Programs
    Key([mod], "f", lazy.spawn(file_manager), desc="Launch File Manager"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch Browser"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch VS Code"),
    # Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),

    # rofi Commands
    Key([mod, 'shift'], "r", lazy.spawn("rofi -show drun")),
    Key([mod, 'shift'], "w", lazy.spawn("rofi -show window")),
    Key([mod, 'shift'], "n", lazy.spawn("networkmanager_dmenu")),
    Key([mod, 'shift'], "f", lazy.spawn("rofi -show filebrowser")),


    # Sound
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -3%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +3%")),

    # Keyboard Backlight
    Key([], "XF86KbdBrightnessDown", lazy.spawn(
        "brightnessctl --device='asus::kbd_backlight' set 1-")),
    Key([], "XF86KbdBrightnessUp", lazy.spawn(
        "brightnessctl --device='asus::kbd_backlight' set 1+")),

    # Monitor Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn(
        "brightnessctl --device='intel_backlight' set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn(
        "brightnessctl --device='intel_backlight' set 10-%")),


    # Music Player Controls

    # Key([], 'XF86AudioPlay', lazy.spawn(
    #     'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify ''/org/mpris/MediaPlayer2 ''org.mpris.MediaPlayer2.Player.PlayPause')),
    # Key([], 'XF86AudioStop',        lazy.spawn(
    #     'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify ''/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop')),
    # Key([], 'XF86AudioNext', lazy.spawn(
    #     'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify ''/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next')),
    # Key([], 'XF86AudioPrev', lazy.spawn(
    # 'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify ''/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous')),

]


# dbus-send - -print-reply - -dest = org.mpris.MediaPlayer2.spotify / org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause
# dbus-send - -print-reply - -dest = org.mpris.MediaPlayer2.spotify / org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next
# dbus-send - -print-reply - -dest = org.mpris.MediaPlayer2.spotify / org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous
# dbus-send - -print-reply - -dest = org.mpris.MediaPlayer2.spotify / org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop
