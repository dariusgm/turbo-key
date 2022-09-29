import keyboard
from art import text2art


class TurboKey:
    def __init__(self):
        self.lock: bool = False
        self.font: str = "tarty8"
        self.hidden: str = text2art("Hidden", font=self.font, chr_ignore=True)
        self.lock_key: str = "f12"
        self.exit_key: str = "esc"
        self.timeout: float = 0.1
        characters = list(map(lambda x: chr(x), range(ord('a'), ord('z') + 1)))
        numbers = list(map(lambda x: f"{x}", range(0, 10)))
        f_keys = list(map(lambda x: f"f{x}", range(1, 13)))
        # Settings for a german keyboard - you may need to change for other languages here.
        # keyboard - key name -> human readable (where possible)
        # make sure the font you are using support everything
        self.other_keys = {
            "esc": "esc",
            "space": "space",
            "backspace": "backspace",
            "enter": "enter",
            "comma": "comma",
            "up": "up",
            "down": "down",
            "left": "left",
            "right": "right",
            "less": "less",
            ".": ".",
            "minus": "-",
            "ö": "oe",
            "ä": "ae",
            "ü": "ae",
            "hash": "hash",
            "plus": "+",
            "apostrophe": "^",
            "ß": "esszet",
            "tab": "tab",
            "#": "hash",
            "altgr+ß": "back-slash",
            "altgr+hash": "single-quote",
            "altgr+plus": "tilde",
            "altgr+less": "pipe",
            "altgr+7": "left curly bracket",
            "altgr+8": "[",
            "altgr+9": "]",
            "altgr+0": "right curly bracket",
            "shift+hash": "single-quote",
            "shift+8": "(",
            "shift+9": ")",
            "shift+0": "=",
            "shift+ß": "?",
            "shift+.": ":",
            "shift+comma": ";",
            "shift+plus": "asterisk",
            "shift+minus": "underscore",
            "shift+less": "bigger"
        }

        self.all_keys = self.flatten([characters, numbers, f_keys, list(self.other_keys.keys())])

        print(text2art("TurboKey", font=self.font, chr_ignore=True))

    @staticmethod
    def flatten(l):
        return [item for sublist in l for item in sublist]

    def register(self):
        print("register keys")
        for key in self.all_keys:
            for ctrl in ["", "ctrl"]:
                for shift in ["", "shift"]:
                    for alt in ["", "alt", "altGr"]:
                        hot_key = []
                        if ctrl != "":
                            hot_key.append(ctrl)

                        if shift != "":
                            hot_key.append(shift)

                        if alt != "":
                            hot_key.append(alt)

                        hot_key.append(key)
                        register_name = "+".join(hot_key)

                        # skip some special combinations for *nix
                        if register_name == "ctrl+c":
                            continue

                        # skip exit_key sequence
                        if register_name == self.exit_key:
                            continue

                        keyboard.add_hotkey(register_name, self.show_key, args=hot_key, trigger_on_release=False,
                                            timeout=0.1)

        keyboard.add_hotkey(self.lock_key, self.toggle_secret)
        print("ready")

    def toggle_secret(self):
        if not self.lock:
            print(self.hidden)
            print(f"TurboKey Disabled, to enable again, press '{self.lock_key}'")

        self.lock = not self.lock

    def wait(self):
        keyboard.wait(self.exit_key)

    def show_key(self, *kwargs):
        if not self.lock:
            elements = []
            for a in kwargs:
                if a in self.other_keys:
                    # map them for better readability
                    elements.append(self.other_keys[a])
                else:
                    elements.append(a)

            print(text2art("+".join(elements), font=self.font, chr_ignore=True))


def main():
    printer = TurboKey()
    printer.register()
    printer.wait()


if __name__ == '__main__':
    main()
