export default function updateStudentGradeByCity(students, city, newGrades) {
  /* eslint-disable no-param-reassign */
  if (Array.isArray(students) === false) {
    return [];
  }
  return students.filter((x) => x.location === city).map((x) => {
    x.grade = 'N/A';
    for (const g of newGrades) {
      if (g.studentId === x.id) {
        x.grade = g.grade;
      }
    }
    return x;
  });
}