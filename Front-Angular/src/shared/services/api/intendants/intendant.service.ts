import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError } from 'rxjs';
import { IntendantDataResponse } from 'src/shared/models/intendant/intendant.models';

@Injectable({
  providedIn: 'root',
})
export class IntendantService {
  constructor(private http: HttpClient) {}

  getIntendant(): Observable<IntendantDataResponse> {
    const token = localStorage.getItem('token');
    return this.http
      .get<IntendantDataResponse>(
        `http://127.0.0.1:8000/api/intendant/get?token=${token}`
      )
      .pipe(
        (data) => {
          return data;
        },
        catchError((error: HttpErrorResponse) => {
          console.error(error);

          throw error;
        })
      );
  }

  findIntendantByEmail(email: string): Observable<IntendantDataResponse> {
    const token = localStorage.getItem('token');
    return this.http
      .get<IntendantDataResponse>(
        `http://127.0.0.1:8000/api/intendant/find-by-email?email=${email}&token=${token}`
      )
      .pipe(
        (data) => {
          return data;
        },
        catchError((error: HttpErrorResponse) => {
          console.error(error);

          throw error;
        })
      );
  }

  registerAdminToSchool(
    id_school: number,
    intendant_email: string
  ): Observable<IntendantDataResponse> {
    const token = localStorage.getItem('token');
    const email = intendant_email;
    const body = { id_school, email, token };
    return this.http.post<IntendantDataResponse>(
      `http://127.0.0.1:8000/api/intendant/register-admin`,
      body
    );
  }
}
