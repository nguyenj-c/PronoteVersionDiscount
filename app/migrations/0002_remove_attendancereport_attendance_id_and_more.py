# Generated by Django 4.0.2 on 2022-02-13 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancereport',
            name='attendance_id',
        ),
        migrations.RemoveField(
            model_name='attendancereport',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='feedbackstaffs',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='feedbackstudent',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='leavereportstaff',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='leavereportstudent',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='notificationstaffs',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='notificationstudent',
            name='student_id',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='AttendanceReport',
        ),
        migrations.DeleteModel(
            name='FeedBackStaffs',
        ),
        migrations.DeleteModel(
            name='FeedBackStudent',
        ),
        migrations.DeleteModel(
            name='LeaveReportStaff',
        ),
        migrations.DeleteModel(
            name='LeaveReportStudent',
        ),
        migrations.DeleteModel(
            name='NotificationStaffs',
        ),
        migrations.DeleteModel(
            name='NotificationStudent',
        ),
    ]
