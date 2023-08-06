 ~> **SGEARNBOT FOR PYTHON**

# Installing

```bash
pip install sgearnbot
```

# Info

You Can Earn Money From Your Python Scripts By This Lib And Your Telegram Account, Just Make User Skip ShortLink and Get Code.

# Using

~> **Replace telegram_id with your Telegram ID from our** [SGEARNBOT](https://t.me/sgearnbot)

```python
#import sgearnbot Library.
from sgearnbot import *
#setup your Telegram Id.
sg = sgearnbot(id="telegram_id")
#Get ShortLink.
link = sg.get_link()
if link:
    print(f"Skip This Link : {link}")
    #wait for user to get code and print it here.
    code = input("write code")
    #check code if correct.
    res = sg.check_code(code)
    if res:
        print("code is correct")
    else:
        print("code is wrong")
else:
    print("no links available now")
```

You Can Use default() Function To Skip Doing All That.

```python
#import sgearnbot Library.
from sgearnbot import *
#setup your Telegram Id.
sg = sgearnbot(id="telegram_id")
#run default() function.
sg.default()
#after this function put your script
```

# Contact Us

Telegram : https://t.me/hellhour
