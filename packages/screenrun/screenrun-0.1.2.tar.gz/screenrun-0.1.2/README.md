# ScreenRun

ScreenRun is a simple process management tool that allows you to keep a process running forever just by adding a single cron job. It utilizes Screen sessions to manage and monitor your processes, making it easy to start, stop, and restart them.

# Installation

To install ScreenRun, run the following command:

```bash
pip install screenrun

```

# Usage

You can use ScreenRun via the command line or in Python scripts.

## Command Line

```bash
# Start a new Screen session with the given name and command
> screenrun execute --name nap sleep 60

# List all running Screen sessions
> screenrun list
nap

# Kill a running Screen session by its name
> screenrun kill --name nap

# Keep a command running indefinitely using the persist option
> screenrun persist --name nap sleep 60

# Start a command in a Screen session if it's not already running
> screenrun persist --name nap sleep 60

```

## Add to cron

To ensure your command keeps running, add the following line to your cron configuration:

```bash
* * * * * screenrun cron sleep 60

```

## Python

You can also use ScreenRun in your Python scripts:

```python
from screenrun import ScreenRun

screenrun = ScreenRun()

screenrun.execute('sleep 60')

```

# Warning for macOS Users

On macOS, the default version of "Screen" is outdated. For ScreenRun to work properly, you need to install the latest GNU version of Screen. You can do this using Homebrew:

```bash
brew install screen

```

Please note that this requires [Homebrew](https://brew.sh/) to be installed on your system. If you don't have Homebrew installed, follow the [installation instructions](https://brew.sh/) before running the above command.


# License

Creative Commons Zero v1.0 Universal
