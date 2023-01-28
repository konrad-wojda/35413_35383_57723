import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { UserDataResponse } from '../models/response_models';

@Injectable({
  providedIn: 'root',
})
export class UsersDataService {
  constructor(private http: HttpClient) {}

  getData(): Observable<UserDataResponse> {
    const token = localStorage.getItem('token');
    return this.http
      .get<UserDataResponse>(`http://127.0.0.1:8000/api/user?token=${token}`)
      .pipe((data) => {
        return data;
      });
  }
}
