import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {
  SchoolCreateData,
  SchoolCreateResponse,
  SchoolData,
} from 'src/shared/models/intendant/school.models';

@Injectable({
  providedIn: 'root',
})
export class SchoolService {
  constructor(private http: HttpClient) {}

  createSchool(payload: SchoolData): Observable<SchoolCreateResponse> {
    const token = localStorage.getItem('token');
    const body: SchoolCreateData = { token, ...payload };

    return this.http.post<SchoolCreateResponse>(
      'http://127.0.0.1:8000/api/school/create',
      body
    );
  }
}
