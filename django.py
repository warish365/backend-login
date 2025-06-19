def calculate_attendance_percentage(student_id, course_id):
    total_classes = Attendance.objects.filter(student_id=student_id, course_id=course_id).count()
    attended_classes = Attendance.objects.filter(student_id=student_id, course_id=course_id, status='present').count()

    attendance_percentage = (attended_classes / total_classes) * 100 if total_classes else 0.0

    # Update or create progress entry
    StudentProgress.objects.update_or_create(
        student_id=student_id,
        course_id=course_id,
        defaults={'attendance_percentage': attendance_percentage}
    )

    return attendance_percentage
