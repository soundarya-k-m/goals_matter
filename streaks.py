from sheets import get_logs_sheet
from datetime import datetime, timedelta


def get_user_dates(username):

    sheet = get_logs_sheet()

    data = sheet.get_all_values()

    dates = []

    for row in data[1:]:

        if len(row) < 2:
            continue

        if row[1].strip().lower() == username.lower():

            try:

                dates.append(
                    datetime.strptime(
                        row[0],
                        "%Y-%m-%d"
                    ).date()
                )

            except:
                pass

    return sorted(
        list(set(dates))
    )


def current_streak(username):

    dates = get_user_dates(username)

    if not dates:
        return 0

    streak = 0

    today = datetime.today().date()

    if today in dates:
        current_day = today

    elif today - timedelta(days=1) in dates:
        current_day = today - timedelta(days=1)

    else:
        return 0

    while current_day in dates:

        streak += 1

        current_day -= timedelta(days=1)

    return streak


def longest_streak(username):

    dates = get_user_dates(username)

    if not dates:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(dates)):

        if (
            dates[i] - dates[i - 1]
        ).days == 1:

            current += 1

            longest = max(
                longest,
                current
            )

        else:

            current = 1

    return longest


def last_active(username):

    dates = get_user_dates(username)

    if not dates:
        return "Never"

    return str(
        dates[-1]
    )