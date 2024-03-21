import random
import time

message_dict = {}

def send_msg(msg: str, delay: int, units: str):
    if not isinstance(delay, int):
        raise Exception("Delay must be an integer.")

    if units not in ["seconds", "minutes", "hours"]:
        raise Exception("Invalid unit. Allowed units are 'seconds', 'minutes', or 'hours'.")

    msg_id = random.randint(100000, 999999)
    unlock_time = time.time()

    if units == "seconds":
        unlock_time += delay
    elif units == "minutes":
        unlock_time += delay * 60
    else:  # units are hours just for clarification
        unlock_time += delay * 3600

    message_dict[msg_id] = (msg, unlock_time)
    print(f"Message ID: {msg_id}")
    return msg_id

def get_msg(msg_id: int):
    if msg_id not in message_dict:
        print("cannot retrieve your message. The message may not exist or more time may need to pass.")
        return False

    msg, unlock_time = message_dict[msg_id]
    current_time = time.time()

    if current_time < unlock_time:
        print("cannot retrieve your message. The message may not exist or more time may need to pass.")
        return False
    else:
        print(msg)
        return True