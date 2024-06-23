import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError } from 'rxjs';
import { IntendantDataResponse } from 'src/shared/models/intendant/intendant.models';

@Injectable({
  providedIn: 'root',
})
export class IntendantService {
  constructor(private http: HttpClient) {}

  findIntendantByEmail(email: string): Observable<IntendantDataResponse> {
    return this.http
      .get<IntendantDataResponse>(
        `http://127.0.0.1:8000/api/intendant/find_by_email?email=${email}`
      )
      .pipe(
        (data) => {
          return data;
        },
        catchError((error: HttpErrorResponse) => {
          return throwError(() => new Error(error.message));
        })
      );
  }
}
