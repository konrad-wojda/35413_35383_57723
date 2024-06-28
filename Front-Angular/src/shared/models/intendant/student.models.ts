export interface AddedStudentResponse {
  id_student: number;
  id_school: number;
  student_first_name: string;
  student_last_name: string;
  student_class: string;
}

export interface StudentsResponse {
  id_student: number;
  full_name: string;
}
