import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {
  AddedStudentResponse,
  StudentsResponse,
} from 'src/shared/models/intendant/student.models';

@Injectable({
  providedIn: 'root',
})
export class StudentService {
  constructor(private http: HttpClient) {}

  getStudents(id_school: number): Observable<StudentsResponse[]> {
    const token = localStorage.getItem('token');
    return this.http
      .get<StudentsResponse[]>(
        `http://127.0.0.1:8000/api/student/get?id_school=${id_school}&token=${token}`
      )
      .pipe((data) => {
        return data;
      });
  }

  AddStudentToSchool(
    id_school: number,
    student_first_name: string,
    student_last_name: string,
    student_class: string
  ): Observable<AddedStudentResponse> {
    const token = localStorage.getItem('token');
    return this.http.post<AddedStudentResponse>(
      `http://127.0.0.1:8000/api/student/add`,
      {
        id_school,
        student_first_name,
        student_last_name,
        student_class,
        token,
      }
    );
  }
}
