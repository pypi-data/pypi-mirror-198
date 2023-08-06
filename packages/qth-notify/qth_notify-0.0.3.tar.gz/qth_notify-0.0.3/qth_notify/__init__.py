"""
Simple utility which enables Linux desktop notifications to be shown via
Qth.
"""

from typing import Any

import asyncio

import platform

import qth

import desktop_notify
from dbus_next import Variant


async def on_notify(_topic: str, message: Any) -> None:
    summary = str(message)
    duration = 30  # Default to 30s
    body = ""
    if isinstance(message, list):
        summary = message[0]
        if len(message) >= 2:
            body = message[1]
        if len(message) >= 3:
            duration = message[2]
    
    notify = desktop_notify.aio.Notify(summary, body)
    
    # In GNOME shell, prevent notifications accumulating in the notifications
    # drawer
    notify.set_hint("transient", Variant("i", 1))
    
    if duration is None:
        notify.set_timeout(0)  # Never expire
    else:
        notify.set_timeout(int(duration * 1000))
    
    await notify.show()
    
    # In GNOME shell, notifications are not hidden after their timeout until
    # they're touched by the mouse. To ensure the timeout is honoured,
    # explicitly close it here.
    if duration is not None:
        await asyncio.sleep(duration)
        await notify.close()


async def async_main(path: str) -> None:
    qth_client = qth.Client(
        f"qth-notify-{platform.node()}",
        f"Show notifications on Linux host {platform.node()}",
    )
    
    await qth_client.register(
        path,
        qth.EVENT_MANY_TO_ONE,
        "Show a notification. Either a string or a list, [summary, body] or [summary, body, duration_seconds].",
    )
    
    await qth_client.watch_event(path, on_notify)
    
    # Run forever
    while True:
        await asyncio.sleep(999)


def main() -> None:
    from argparse import ArgumentParser
    parser = ArgumentParser("Trigger Linux destop notifications via Qth")
    parser.add_argument("qth_path")
    args = parser.parse_args()
    asyncio.run(async_main(args.qth_path))


if __name__ == "__main__":
    main()
