from datetime import datetime, timedelta

class AppController:
    def calculate(self):
        journey = timedelta(hours=8, minutes=0)
        now = datetime.now()

        firstIn = now.replace(hour=8, minute=0)
        firstOut = now.replace(hour=12, minute=0)

        secondIn = now.replace(hour=13, minute=0)
        secondOut = now.replace(hour=17, minute=0)

        result = (firstOut - firstIn) + (secondOut - secondIn)

        seconds = result.total_seconds()
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return "Worked: %02d:%02d" % (hours, minutes)
