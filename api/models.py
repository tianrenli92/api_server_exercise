from django.db import models

# college name: https://www.bu.edu/reg/registration/abbreviations/
# generator: static/constant_generator.xlsx

BUA = 'BUA'
CAS = 'CAS'
CFA = 'CFA'
CGS = 'CGS'
COM = 'COM'
ENG = 'ENG'
EGS = 'EGS'
EOP = 'EOP'
GMS = 'GMS'
GRS = 'GRS'
HUB = 'HUB'
KHC = 'KHC'
LAW = 'LAW'
MED = 'MED'
MET = 'MET'
OTP = 'OTP'
PDP = 'PDP'
QST = 'QST'
SAR = 'SAR'
SED = 'SED'
SDM = 'SDM'
SHA = 'SHA'
SPH = 'SPH'
SSW = 'SSW'
STH = 'STH'
SUM = 'SUM'
UNI = 'UNI'
XRG = 'XRG'
COLLEGE_CHOICES = (
    (BUA, 'Boston University Academy'),
    (CAS, 'College of Arts & Sciences'),
    (CFA, 'College of Fine Arts'),
    (CGS, 'College of General Studies'),
    (COM, 'College of Communication'),
    (ENG, 'College of Engineering'),
    (EGS, 'College of Engineering and Graduate School of Arts & Sciences'),
    (EOP, 'Center for English Language & Orientation Programs (CELOP)'),
    (GMS, 'Graduate Medical Sciences'),
    (GRS, 'Graduate School of Arts & Sciences'),
    (HUB, 'Hub Office, General Education'),
    (KHC, 'Kilachand Honors College'),
    (LAW, 'School of Law'),
    (MED, 'School of Medicine'),
    (MET, 'Metropolitan College'),
    (OTP, 'Officer Training Program'),
    (PDP, 'Physical Development Program'),
    (QST, 'Questrom School of Business'),
    (SAR, 'Sargent College of Health & Rehabilitation Sciences'),
    (SED, 'School of Education'),
    (SDM, 'Henry M. Goldman School of Dental Medicine'),
    (SHA, 'School of Hospitality Administration'),
    (SPH, 'School of Public Health'),
    (SSW, 'School of Social Work'),
    (STH, 'School of Theology'),
    (SUM, 'Summer Term Program'),
    (UNI, 'The University Professors'),
    (XRG, 'Cross Registration'),
)

# school year
FRESHMAN = 1
SOPHOMORE = 2
JUNIOR = 3
SENIOR = 4
GRADUATE = 5
YEAR_CHOICES = (
    (FRESHMAN, 'Freshman'),
    (SOPHOMORE, 'Sophomore'),
    (JUNIOR, 'Junior'),
    (SENIOR, 'Senior'),
    (GRADUATE, 'Graduate'),
)


class Student(models.Model):
    # create local constants the same as the globals
    COLLEGE_CHOICES = COLLEGE_CHOICES
    YEAR_CHOICES = YEAR_CHOICES

    name = models.CharField(max_length=64)
    college = models.CharField(max_length=3, choices=COLLEGE_CHOICES)
    year = models.IntegerField(choices=YEAR_CHOICES)
    # store course list in json as for now
    courses = models.TextField()

# class Course(models.Model):
#     COLLEGE_CHOICES = COLLEGE_CHOICES
#
#     semester = models.IntegerField(default=20194, db_index=True)
#     # student link semester format:
#     # 20193: Fall 2018; 20194: Spring 2019
#     college = models.CharField(max_length=3, choices=COLLEGE_CHOICES, db_index=True)
#     department = models.CharField(max_length=3)
#     number = models.IntegerField()
#     section = models.CharField(max_length=3)
#     credit = models.DecimalField(max_digits=3, decimal_places=1)
#     title = models.CharField(max_length=64)
#     professor_name = models.CharField(max_length=64)
#     professor_link = models.CharField(max_length=64, blank=True)
#     type = models.CharField(max_length=64)
#     building = models.CharField(max_length=3)
#     room = models.CharField(max_length=64)
#     day = models.CharField(max_length=64)
#     start_time = models.CharField(max_length=64)
#     stop_time = models.CharField(max_length=64)
#     note = models.CharField(max_length=256)
#     description = models.TextField()
#
#
# class StudentCourse(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
