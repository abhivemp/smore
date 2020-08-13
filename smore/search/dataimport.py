import os, csv
from search.models import collegeCourse

def changeName(s):
    lName = s[0 : s.index(",")]
    fName = s[s.index(",") + 1 :]
    return str(fName + lName)


os.chdir("C:\\Users\\abhij\\Desktop\\Workshop\\smore\\smore\\search")
with open('courseInfoData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        newRow = changeName(row['professor'])
        p = collegeCourse(class_id=row['class_id'], course_code=row['course_code'], professor=newRow, day=row['day'], time=row['time'])
        p.save()
