"""
复读机示例。
"""

from cyanide import Session, Ticket
from cyanide.event.events import ChannelMessageReceivedEvent
from cyanide.model import Message

session = Session(
    "https://sandbox.api.sgroup.qq.com/",
    Ticket("{app_id}", "{token}")
)


@session.on(ChannelMessageReceivedEvent)
async def message_received(data: Message):
    await data.reply(data)

session.run()
