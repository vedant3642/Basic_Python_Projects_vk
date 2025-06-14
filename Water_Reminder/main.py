import time
from plyer import notification
from datetime import datetime

try:
    while True:
        # Get current time
        current_time = datetime.now().strftime("%I:%M %p")

        # Send notification
        notification.notify(
            title="💧 Hydration Reminder",
            message=f"It's {current_time}. Time to drink water and stay hydrated!",
            timeout=10  # seconds
        )

        # Wait for 1 hour (3600 seconds)
        time.sleep(3600)

except KeyboardInterrupt:
    print("\nWater reminder stopped. Stay healthy! 💧")
