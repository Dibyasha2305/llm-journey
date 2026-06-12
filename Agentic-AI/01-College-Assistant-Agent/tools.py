from langchain.tools import tool

@tool
def attendance_calculator(
    total_classes: int,
    attended_classes: int
):
    """
    Calculate attendance percentage
    and exam eligibility.
    """

    attendance = (
        attended_classes / total_classes
    ) * 100

    if attendance >= 75:
        status = "Eligible for Exam"
    else:
        status = "Not Eligible for Exam"

    return {
        "attendance_percentage": round(attendance, 2),
        "status": status
    }

@tool
def result_calculator(
    m1: int,
    m2: int,
    m3: int,
    m4: int,
    m5: int
):
    """
    Calculate average marks,
    grade and pass/fail status.
    """

    average = (m1 + m2 + m3 + m4 + m5) / 5

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"

    return {
        "average_marks": round(average, 2),
        "grade": grade,
        "result": result
    }


@tool
def fee_balance_calculator(
    total_fee: int,
    amount_paid: int
):
    """
    Calculate pending fee amount.
    """

    pending_fee = total_fee - amount_paid

    return {
        "pending_fee": pending_fee
    }


@tool
def library_fine_calculator(
    delayed_days: int
):
    """
    Calculate library fine.
    Fine = 5 rupees per delayed day.
    """

    fine = delayed_days * 5

    return {
        "fine_amount": fine
    }


@tool
def hostel_fee_calculator(
    monthly_fee: int,
    months_stayed: int
):
    """
    Calculate total hostel fee.
    """

    total_fee = monthly_fee * months_stayed

    return {
        "hostel_fee": total_fee
    }


students = {
    "101": {
        "name": "Rahul",
        "branch": "CSE",
        "year": "3rd Year"
    },
    "102": {
        "name": "Priya",
        "branch": "IT",
        "year": "2nd Year"
    },
    "103": {
        "name": "Aman",
        "branch": "ECE",
        "year": "4th Year"
    }
}
@tool
def student_info(student_id: str):
    """
    Retrieve student details using student ID.
    """

    student = students.get(student_id)

    if student:
       return student

    return {
         "error": "Student not found"
}