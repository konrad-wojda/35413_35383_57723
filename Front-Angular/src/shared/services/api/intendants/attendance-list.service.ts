import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {
  AttendanceListRequest,
  AttendanceListResponse,
} from 'src/shared/models/intendant/attendance-list.models';
@Injectable({
  providedIn: 'root',
})
export class AttendanceListService {
  constructor(private http: HttpClient) {}

  addSingleDayAttendance(payload: AttendanceListRequest): Observable<boolean> {
    payload.token = localStorage.getItem('token');

    return this.http.post<boolean>(
      `http://127.0.0.1:8000/api/attendance-list/add-single`,
      {
        ...payload,
      }
    );
  }

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
