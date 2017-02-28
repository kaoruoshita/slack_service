from slackclient import SlackClient
import json

def _send_message(api_key, channel_id, message):
    slack_client = SlackClient(api_key)
    res = slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        # username='k.oshita',
        # icon_emoji=':robot_face:'
       # as_user = True
    )
    return res

def _format_options(options):
  my_dict = {}
  if options:
    for option in options:
        my_dict[option['key']] = option['val']

  return my_dict



def handle(event, context):
    data = _format_options(event.get("options", None))
    message = data.get("Message")
    api_key = data.get("API Key")
    channel_id = data.get("Channel ID")
    res = _send_message(api_key, channel_id, message)

    return res
