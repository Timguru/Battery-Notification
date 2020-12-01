import psutil
from plyer import notification
import time

#from psutil we will import the
#sensor_battery class
#will return null if there is no battery
battery = psutil.sensors_battery()


while(True):
    percent = battery.percent

    notification.notify(
        title = "Battery Percentage",
        message = str(percent) + "% Battery remaining",
        timeout = 10
    )

    time.sleep(60 * 5)

    continue