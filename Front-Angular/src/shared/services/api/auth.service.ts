import { Injectable } from '@angular/core';
import { catchError, tap } from 'rxjs/operators';
import { BehaviorSubject, Observable, throwError } from 'rxjs';
import { ApiService } from './api.service';
import { Router } from '@angular/router';
import { UserStateService } from '../states/UserStateService';
import { UserService } from './intendants/user.service';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private _isLoggedIn$ = new BehaviorSubject<boolean>(false);
  isLoggedIn$ = this._isLoggedIn$.asObservable();

  constructor(
    private apiService: ApiService,
    private userStateService: UserStateService,
    private userService: UserService,
    private router: Router
  ) {
    const token = localStorage.getItem('token');
    this._isLoggedIn$.next(!!token);
  }

  login(email: string, password: string) {
    return this.apiService.login(email, password).pipe(
      catchError((error) => {
        return throwError(() => error);
      }),
      tap((response: any) => {
        if (response.token === undefined) {
          this._isLoggedIn$.next(false);
          return false;
        }
        if (response.status_code == 200) {
          localStorage.setItem('token', response.token);
          this.getUserData();
          this._isLoggedIn$.next(true);
          return true;
        }

        this._isLoggedIn$.next(false);
        return false;
      })
    );
  }

  isLoggedIn(): Observable<boolean> {
    return this.isLoggedIn$;
  }

  getUserData() {
    this.userService.getData().subscribe((userData) => {
      this.userStateService.setCurrentUser(userData);
    });
  }

  editUser(body: any) {
    body['id_user'] = localStorage.getItem('id_user');
    body['token'] = localStorage.getItem('token');

    return this.apiService.editUser(body).pipe().subscribe();
  }

  deleteUser(body: any) {
    body['id_user'] = parseInt(localStorage.getItem('id_user'));

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
    sessionStorage.clear();
  }
}
