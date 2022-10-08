export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
    let result;
    const students = getListStudents.filter((stud) => stud.location === city);
    return students.map((student) => {
      const studentgradebyId = newGrades.filter((element) => element.studentId === student.id);
      try {
        result = student;
        if (studentgradebyId[0].grade) { result.grade = studentgradebyId[0].grade; }
      } catch (e) {
        result.grade = 'N/A';
      }
      return result;
    });
  }
