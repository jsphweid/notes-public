# Daemon

computer program that runs as a background process rather than being under direct control of the active user (yes pretty much straight from [here](https://en.wikipedia.org/wiki/Daemon_(computing)))

- typically end in `d` (like `supervisord`?)

"daemon" has something to do with silent, or running silently?

on linux, systemD/Init daemon runs on boot pretty much, starts rest of daemon and graphical settings

no interaction with user, only use log files

it's a process (but not all processes are daemons, of course)