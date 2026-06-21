from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

import pandas as pd

from sheets import get_logs_sheet


def generate_report(username):

    filename = f"{username}_weekly_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Goals Matter Weekly Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    sheet = get_logs_sheet()

    data = sheet.get_all_values()

    df = pd.DataFrame(
        data[1:],
        columns=data[0]
    )

    df = df[
        df["Username"].str.lower()
        == username.lower()
    ]

    if len(df) == 0:

        content.append(
            Paragraph(
                "No data available.",
                styles["Normal"]
            )
        )

        doc.build(content)

        return filename

    df["Score"] = pd.to_numeric(
        df["Score"],
        errors="coerce"
    ).fillna(0)

    avg_score = round(
        df["Score"].mean(),
        1
    )

    best_score = int(
        df["Score"].max()
    )

    total_logs = len(df)

    content.append(
        Paragraph(
            f"User: {username}",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Total Logs: {total_logs}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Average Score: {avg_score}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Best Score: {best_score}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Keep pushing towards your goals!",
            styles["Heading3"]
        )
    )

    doc.build(content)

    return filename