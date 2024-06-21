# Moon Phase CLI

### High Level Design

Moon Phase is a simple CLI which will output to the console some basic information about the phase of the moon and other astrological information and concordences for a given time stamp. It is lightweight enough to be suitable for invocation on a login terminal on start up.

Basic invocation will output moon phase, timings of the next quarter phase, and any "interesting" planetary movements at the time of invocation.
Other options allow specifying a different timestamp.
Other display options allow displaying more or less information and potentially other display formats.

### Detailed brainstorm

Program can be invoked with `moon`.

A plain invocation will print to the console the current moon phase.
Specifying a timestamp with `-t/--timestamp 2000/1/4` will display the moon phase at 12:01 AM on January 4th, 2000.
