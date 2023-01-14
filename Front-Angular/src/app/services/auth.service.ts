import { Injectable } from '@angular/core';
import { catchError, tap } from 'rxjs/operators';
import { BehaviorSubject, Observable } from 'rxjs';
import { ApiService } from './api.service';
import { Router } from '@angular/router';
import { HttpErrorResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private _isLoggedIn$ = new BehaviorSubject<boolean>(false);
  isLoggedIn$ = this._isLoggedIn$.asObservable();

  constructor(private apiService: ApiService, private router: Router) {
    const token = localStorage.getItem('token');
    this._isLoggedIn$.next(!!token);
  }

  login(email: string, password: string) {
    return this.apiService.login(email, password).pipe(
      tap((response: any) => {
        if (response.token === undefined) {
          this._isLoggedIn$.next(false);
          return false;
        }
        if (response.status_code == 200) {
          localStorage.setItem('token', response.token);
          localStorage.setItem('user_id', response.user_id);
          this._isLoggedIn$.next(true);
          return true;
        }

        this._isLoggedIn$.next(false);
        return false;
      })
    );
  }

  editUser(body: any) {
    body['user_id'] = localStorage.getItem('user_id');
    body['token'] = localStorage.getItem('token');

    return this.apiService.editUser(body).pipe().subscribe();
  }

  deleteUser(body: any) {
    body['user_id'] = parseInt(localStorage.getItem('user_id'));

    return this.apiService
      .deleteUser(body)
      .pipe(
        tap(
          (response: any) => {
            if (response.status_code == 200) {
              this.router.navigate(['/']);
              this.logout();
              this._isLoggedIn$.next(false);

              return true;
            }
            return false;
          },
          (error) => {
            alert(error.error.detail);
          }
        )
      )
      .subscribe();
  }

  logout() {
    localStorage.clear();
  }
}
