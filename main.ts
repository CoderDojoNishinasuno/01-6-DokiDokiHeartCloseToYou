radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    きょり = radio.receivedPacket(RadioPacketProperty.SignalStrength) * -1
})
let きょり = 0
きょり = 999
radio.setGroup(1)
basic.forever(function on_forever() {
    if (きょり < 55) {
        basic.showIcon(IconNames.Heart, 50)
        basic.showIcon(IconNames.SmallHeart, 50)
    } else if (きょり < 65) {
        basic.showIcon(IconNames.Heart, 150)
        basic.showIcon(IconNames.SmallHeart, 150)
    } else if (きょり < 75) {
        basic.showIcon(IconNames.Heart, 250)
        basic.showIcon(IconNames.SmallHeart, 250)
    } else {
        basic.showIcon(IconNames.Heart, 500)
        basic.showIcon(IconNames.SmallHeart, 500)
    }
    
})
basic.forever(function on_forever2() {
    radio.sendNumber(0)
    basic.pause(500)
})
