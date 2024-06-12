import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { UserDataResponse } from '../../models/intendant/user.models';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  constructor(private http: HttpClient) {}

  getData(): Observable<UserDataResponse> {
    const token = localStorage.getItem('token');
    return this.http
      .get<UserDataResponse>(
        `http://127.0.0.1:8000/api/user/get?token=${token}`
      )
      .pipe((data) => {
        return data;
      });
  }

  findUser(): Observable<UserDataResponse> {
    const token = localStorage.getItem('token');
    return this.http
      .get<UserDataResponse>(
        `http://127.0.0.1:8000/api/user/get?token=${token}`
      )
      .pipe((data) => {
        return data;
      });
  }
}
