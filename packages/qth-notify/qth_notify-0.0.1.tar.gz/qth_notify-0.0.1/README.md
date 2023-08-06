qth-notify
==========

A trivial Qth interface enabling Linux desktop notifications to be sent via
Qth.

Usage::

    $ qth-notify path/to/notify/endpoint

Then to show notifications:

    $ qth path/to/notify/endpoint '"Hello, world!"'
    $ qth path/to/notify/endpoint '["Title here", "Hello, world!"]'
    $ qth path/to/notify/endpoint '["Title here", "Hello, world!", 5]'  # Show for 5 seconds
