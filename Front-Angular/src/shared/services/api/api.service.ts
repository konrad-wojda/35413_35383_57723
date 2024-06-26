import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  constructor(private http: HttpClient) {}
  headers = new HttpHeaders()
    .set('accept', 'application/json')
    .set('Content-Type', 'application/json');

  login(email: string, password: string) {
    const body = { email, hashed_password: password };
    return this.http.post('http://127.0.0.1:8000/api/user/login', body);
  }

  register(email: string, password: string, repeat_password: string): any {
    const body = { email, hashed_password: password, repeat_password };
    return this.http.post('http://127.0.0.1:8000/api/user/register', body);
  }

  editUser(body) {
    return this.http.patch('http://127.0.0.1:8000/api/user/edit', body);
  }

  deleteUser(body) {
    return this.http.delete('http://127.0.0.1:8000/api/user/delete', { body });
  }
}
