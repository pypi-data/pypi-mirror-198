"""
Simple utility which enables Linux desktop notifications to be shown via
Qth.
"""

from typing import Any

import asyncio

import platform

import qth

import desktop_notify


async def on_notify(_topic: str, message: Any) -> None:
    summary = str(message)
    duration = None
    body = ""
    if isinstance(message, list):
        summary = message[0]
        if len(message) >= 2:
            body = message[1]
        if len(message) >= 3:
            duration = message[2]
    
    notify = desktop_notify.aio.Notify(summary, body)
    if duration is not None:
        notify.set_timeout(int(duration * 1000))
    await notify.show()


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
