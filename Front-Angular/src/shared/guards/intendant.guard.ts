import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { IntendantStateService } from '../services/states/IntendantStateService';
import { IntendantService } from '../services/api/intendants/intendant.service';
import { Observable, map, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class IntendantGuard {
  constructor(
    private intendantService: IntendantService,
    private intendantStateService: IntendantStateService,
    private router: Router
  ) {}

  canActivate(): Observable<boolean> {
    // @TODO check state, than make call to api
    if (this.intendantStateService.currentIntendant) return of(true);

    return this.intendantService.getIntendant().pipe(
      map((userData) => {
        if (userData) {
          this.intendantStateService.setCurrentIntendant(userData);

          return true;
        } else {
          this.router.navigate(['/login']);
          return false;
        }
      })
    );
  }
}
