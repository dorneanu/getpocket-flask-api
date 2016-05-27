A simple **REST** API for [getpocket](https://getpocket.com) using [Flask](http://flask.pocoo.org) and
[pocket-api](https://pypi.python.org/pypi/pocket-api/). This tool actually uses **pocket-api** to 
provide a RESTful API to [getpocket's API](https://getpocket.com/developer/).

# Installation

Create a virtual environment and install the requirements:

```.shell
$ mkdir env
$ virtualenv env
...
$ source env/bin/activate
$ pip install -r requirements.txt
..
```

# Run

```.shell
$ FLASK_CONFIG_FILE=config.cfg python api.py
 * Running on http://127.0.0.1:5556/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 187-149-471
```

Now you can access:

* http://127.0.0.1:5556/pocket/get/<insert tag here>/<number of articles>

Examples:

* http://127.0.0.1:5556/pocket/get/android
* http://127.0.0.1:5556/pocket/get/android/10

