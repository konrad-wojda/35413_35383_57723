import { Injectable } from '@angular/core';
import { IntendantDataResponse } from 'src/shared/models/intendant/intendant.models';

@Injectable({
  providedIn: 'root',
})
export class IntendantStateService {
  // @TODO ... session Storage, srly?
  setCurrentIntendant(user: IntendantDataResponse) {
    sessionStorage.setItem('IntendantStateService', JSON.stringify(user));
  }

  get currentIntendant(): IntendantDataResponse | null {
    return JSON.parse(sessionStorage.getItem('IntendantStateService'));
  }
}
