def on_received_number(receivedNumber):
    global きょり
    きょり = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) * -1
radio.on_received_number(on_received_number)

きょり = 0
きょり = 999
radio.set_group(1)

def on_forever():
    if きょり < 55:
        basic.show_icon(IconNames.HEART, 50)
        basic.show_icon(IconNames.SMALL_HEART, 50)
    elif きょり < 70:
        basic.show_icon(IconNames.HEART, 150)
        basic.show_icon(IconNames.SMALL_HEART, 150)
    elif きょり < 85:
        basic.show_icon(IconNames.HEART, 250)
        basic.show_icon(IconNames.SMALL_HEART, 250)
    else:
        basic.show_icon(IconNames.HEART, 500)
        basic.show_icon(IconNames.SMALL_HEART, 500)
basic.forever(on_forever)

def on_forever2():
    radio.send_number(0)
    basic.pause(100)
basic.forever(on_forever2)
