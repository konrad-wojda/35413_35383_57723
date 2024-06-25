import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { UserDataResponse } from 'src/shared/models/intendant/user.models';

@Injectable({
  providedIn: 'root',
})
export class UserStateService {
  private _userData$ = new BehaviorSubject<UserDataResponse>(null);
  userData$ = this._userData$.asObservable();
  // @TODO ... session Storage, srly?
  setCurrentUser(user: UserDataResponse) {
    sessionStorage.setItem('UserStateService', JSON.stringify(user));
    this._userData$.next(user);
  }

  get currentUser(): UserDataResponse | null {
    return JSON.parse(sessionStorage.getItem('UserStateService'));
  }
}
