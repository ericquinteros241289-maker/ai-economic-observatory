import datetime

def write_report(analysis):

    today = datetime.date.today()

    filename = f"reports/daily/report_{today}.txt"

    with open(filename, "w") as f:

        f.write("Daily Economic Intelligence Report\n\n")

        for item in analysis:
            f.write(item + "\n")

    return filename
