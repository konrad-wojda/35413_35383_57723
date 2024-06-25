import { Injectable } from '@angular/core';
import { UserDataResponse } from 'src/shared/models/intendant/user.models';

@Injectable({
  providedIn: 'root',
})
export class UserStateService {
  // @TODO ... session Storage, srly?
  setCurrentUser(user: UserDataResponse) {
    sessionStorage.setItem('UserStateService', JSON.stringify(user));
  }

  get currentUser(): UserDataResponse | null {
    return JSON.parse(sessionStorage.getItem('UserStateService'));
  }
}
