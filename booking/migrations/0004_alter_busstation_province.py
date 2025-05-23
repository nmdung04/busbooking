# Generated by Django 5.1.4 on 2025-03-26 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0003_remove_busstation_contact_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="busstation",
            name="province",
            field=models.CharField(
                choices=[
                    ("DNANG", "Đà Nẵng"),
                    ("NAN", "Nghệ An"),
                    ("QNAM", "Quảng Nam"),
                    ("HNOI", "Hà Nội"),
                    ("HCMINH", "Hồ Chí Minh"),
                    ("TTTHUE", "Thừa Thiên Huế"),
                    ("QNGAI", "Quảng Ngãi"),
                    ("QTRI", "Quảng Trị"),
                    ("QBINH", "Quảng Bình"),
                    ("HTINH", "Hà Tĩnh"),
                    ("DLAT", "Đà Lạt"),
                ],
                max_length=50,
            ),
        ),
    ]
