import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AttendanceListResponse } from 'src/shared/models/intendant/attendance-list.models';
@Injectable({
  providedIn: 'root',
})
export class AttendanceListService {
  constructor(private http: HttpClient) {}

  // AddSingleDaySchool(
  //   id_school: number,
  //   student_first_name: string,
  //   student_last_name: string,
  //   student_class: string
  // ): Observable<AddedStudentResponse> {
  //   const token = localStorage.getItem('token');
  //   return this.http.post<AddedStudentResponse>(
  //     `http://127.0.0.1:8000/api/attendance-list/add-single`,
  //     {
  //       id_school,
  //       student_first_name,
  //       student_last_name,
  //       student_class,
  //       token,
  //     }
  //   );
  // }

  getAttendanceList(
    id_school: number,
    date: string = '2024-06-18'
  ): Observable<AttendanceListResponse[]> {
    const token = localStorage.getItem('token');

    return this.http
      .get<AttendanceListResponse[]>(
        `http://127.0.0.1:8000/api/attendance-list/get?token=${token}&date=${date}&id_school=${id_school}`
      )
      .pipe((data) => {
        return data;
      });
  }
}
