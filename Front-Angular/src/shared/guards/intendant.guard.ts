import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/shared/services/api/auth.service';
import { UserService } from 'src/shared/services/api/intendants/user.service';
import { UserStateService } from 'src/shared/services/states/UserStateService';

@Injectable({
  providedIn: 'root',
})
export class IntendantGuard {
  constructor(
    private authService: AuthService,
    private userService: UserService,
    private userStateService: UserStateService,
    private router: Router
  ) {}

  canActivate(): boolean {
    // @TODO check state, than make call to api
    // if (this.userStateService.currentUser) return true;
    // if (this.authService.isLoggedIn()) {
    //   this.userService.getData().subscribe((userData) => {
    //     this.userStateService.setCurrentUser(userData);
    //   });
    //   return true;
    // } else {
    //   this.router.navigate(['/login']);
    //   return false;
    // }
    return true;
  }
}
