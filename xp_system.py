import pandas as pd

from sheets import get_logs_sheet


def calculate_xp(username):

    sheet = get_logs_sheet()

    data = sheet.get_all_values()

    if len(data) <= 1:
        return 0

    df = pd.DataFrame(
        data[1:],
        columns=data[0]
    )

    user_df = df[
        df["Username"].astype(str).str.lower()
        == str(username).lower()
    ]

    xp = 0

    for _, row in user_df.iterrows():

        if row["Workout"] == "Yes":
            xp += 20

        try:
            if float(row["Study"]) >= 5:
                xp += 20
        except:
            pass

        try:
            if float(row["Water Intake"]) >= 3:
                xp += 10
        except:
            pass

        try:
            if float(row["Sleep"]) >= 7:
                xp += 20
        except:
            pass

        try:
            if int(row["Score"]) == 100:
                xp += 50
        except:
            pass

    return xp


def get_level(xp):

    if xp >= 5000:
        return "🚀 Astronaut", 10

    elif xp >= 4000:
        return "👑 Legend", 9

    elif xp >= 3000:
        return "🥇 Master", 8

    elif xp >= 2000:
        return "🥈 Elite", 7

    elif xp >= 1500:
        return "🥉 Pro", 6

    elif xp >= 1000:
        return "🔥 Advanced", 5

    elif xp >= 600:
        return "⭐ Skilled", 4

    elif xp >= 300:
        return "🌱 Learner", 3

    elif xp >= 100:
        return "🎯 Beginner", 2

    else:
        return "👶 Rookie", 1