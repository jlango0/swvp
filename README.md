# swvp.py

## What does it mean?
The (rather catchy) name **swvp** is taken from the first 3 letters of the zsh command:

    % SW_Vers

_**P**_lus checking for macOS updates using Python, via requests and bs4.

The command [sw_vers](https://www.unix.com/man_page/osx/1/sw_vers/)  returns the currently installed version of macOS, among other values that are less relevant here.

In Python, platform.mac_ver() returns a tuple, where index 0 provides the same macOS version info as % sw_vers itself.

## Why does swvp.py exist?
Prior to writing swvp.py, I would often load the [Apple security releases](https://support.apple.com/en-us/100100) page, then confirm their page still matched the output of sw_vers in my Terminal... which wasn't terribly efficient.

It's also worth mentioning I started this habit because Apple was no longer reliably notifying me about newly released OS patches.  Their notifications often come at least 1 day after the update has been released, sometimes even later.

🚨 But waiting for Apple to get around to notifying users is not worth the risk, as [Joshua Long of the Mac Security Blog](https://www.intego.com/mac-security-blog/urgent-macos-sequoia-15-4-1-ios-18-4-1-address-2-zero-day-vulnerabilities/)  explains, in excellent detail. 🚨

Automating this process brings me one step closer to staying on top of macOS patches.

## Final notes
The current version of swvp.py is rudimentary, but has done the job so far. I have various improvements planned, including setting up a macOS-style cronjob once I clarify more details about [launchd](https://support.apple.com/en-us/100100).

But in the meantime, it's nice to at least automate this update checking workflow.

Hopefully it can help some other folks, too.
