from platform import system

if system() == 'Windows':
    from devoud.browser.utils.os.win32_utils import make_shortcut
elif system() == 'Darwin':
    from devoud.browser.utils.os.mac_utils import make_shortcut
else:
    from devoud.browser.utils.os.linux_utils import make_shortcut


