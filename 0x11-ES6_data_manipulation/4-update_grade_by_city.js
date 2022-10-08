export default function updateStudentGradeByCity(arrayofstudents, city, newgrades) {
  return arrayofstudents.filter((i) => i.location === city).map((i) => {
    const [newGrade] = newgrades.filter((item) => item.studentId === i.id);
    return { ...i, grade: newGrade ? newGrade.grade : 'N/A' };
  });
}