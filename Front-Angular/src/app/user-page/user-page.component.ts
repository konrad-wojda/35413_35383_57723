import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/intendants/user.service';
import { UserDataResponse } from '../models/intendant/user.models';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-user-page',
  templateUrl: './user-page.component.html',
  styleUrls: ['./user-page.component.scss'],
})
export class UserPageComponent implements OnInit {
  user: UserDataResponse;

  constructor(
    private usersDataService: UserService,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    this.usersDataService.getData().subscribe((data) => {
      this.user = { ...data };
    });
  }

  delete(email: string) {
    var result = prompt(
      'Are You sure to delete account?',
      'Write Your password.'
    );
    if (result) {
      this.authService.deleteUser({
        email: email,
        hashed_password: result,
        repeat_password: result,
      });
    }
  }
}
