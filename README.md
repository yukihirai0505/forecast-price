## Setup

```
$ make build
$ brew install ta-lib
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install --no-cache-dir -r requirements.txt
# Edit matplotlibrc file backend macosx => Tkagg ref: https://qiita.com/Kodaira_/items/1a3b801c7a5a41c9ce49
$ python prophet.py
```

## Resources

- [prophet](https://github.com/facebook/prophet)
- [pyenvとvirtualenvで環境構築した時にmatplotlib.pyplotが使えなかった時の対処法](https://qiita.com/Kodaira_/items/1a3b801c7a5a41c9ce49)