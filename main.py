from slackclient import SlackClient
import json

def _send_message(channel_id, message):
    res = slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        # username='k.oshita',
        # icon_emoji=':robot_face:'
       # as_user = True
    )

def handle(event, context):
    _send_message(channel_id, message)

handle(1,1)
