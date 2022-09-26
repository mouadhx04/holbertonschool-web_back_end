export default function getListStudentIds(objs) {
    if (Array.isArray(objs) === false) {
      return [];
    }
    return objs.map((x) => x.id);
  }
