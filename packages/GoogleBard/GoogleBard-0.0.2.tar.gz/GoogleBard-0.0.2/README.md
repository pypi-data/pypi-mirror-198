# Bard
Reverse engineering of Google's Bard chatbot

## Authentication
Go to https://bard.google.com/

- F12 for console
- Copy the values
  - Session: `cookieStore.get("_U").then(result => console.log(result.value))` 
  - At: `window.WIZ_global_data.SNlM0e` 

```bash
$ python3 -m Bard -h
usage: Bard.py [-h] --session SESSION --at AT

options:
  -h, --help         show this help message and exit
  --session SESSION  __Secure-1PSID cookie.
  --at AT            window.WIZ_global_data.SNlM0e
```

[Developer Documentation](https://github.com/acheong08/Bard/blob/main/DOCUMENTATION.md)
