def calculate_fine(late_days, book_type="reference", premium_member=False):

    if book_type == "reference":
        fine = late_days * 20

    else:
        if late_days <= 5:
            fine = late_days * 5
        else:
            fine = (5 * 5) + ((late_days - 5) * 10)

    if premium_member:
        fine = fine * 0.80

    return fine
print(calculate_fine(3))
print(calculate_fine(7))
print(calculate_fine(10, "reference"))
print(calculate_fine(10, "standard", True))
