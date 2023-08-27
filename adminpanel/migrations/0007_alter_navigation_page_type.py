# Generated by Django 4.2.3 on 2023-08-02 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0006_alter_navigation_page_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigation',
            name='page_type',
            field=models.CharField(blank=True, choices=[('Home', 'Home'), ('Vision', 'Vision'), ('Mission', 'Mission'), ('Home/About', 'Home/About'), ('Documents', 'Documents'), ('About Company', 'About Company'), ('Registration/Approval', 'Registration/Approval'), ('About', 'About'), ('Our Message', 'Our Message'), ('Our Commitment', 'Our Commitment'), ('Pop', 'Pop'), ('Contact', 'Contact'), ('Organizational Chart', 'Organizational Chart'), ('Demand Letter', 'Demand Letter'), ('Job Seeker', 'Job Seeker'), ('Recruiting Procedure', 'Recruiting Procedure'), ('Recruiting Documents', 'Recruiting Documents'), ('Gallery', 'Gallery'), ('Slider', 'Slider'), ('Service', 'Service'), ('Amity/Service', 'Amity/Service'), ('Newspaper Vacancy', 'Newspaper Vacancy'), ('Our Service', 'Our Service'), ('Requirement', 'Requirement'), ('Group', 'Group'), ('Normal', 'Normal'), ('Talent', 'Talent'), ('UNSKILLED', 'UNSKILLED'), ('THE PROFESSIONALS', 'THE PROFESSIONALS'), ('SEMI-SKILLED', 'SEMI-SKILLED'), ('SKILLED', 'SKILLED'), ('HIGHLYSKILLED', 'HIGHLYSKILLED'), ('TESTIMONIAL', 'TESTIMONIAL'), ('COUNTRIES', 'COUNTRIES')], max_length=50, null=True),
        ),
    ]
