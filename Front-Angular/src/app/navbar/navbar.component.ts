import { Component, OnInit } from '@angular/core';
import { UserDataResponse } from 'src/shared/models/intendant/user.models';
import { AuthService } from 'src/shared/services/api/auth.service';
import { IntendantService } from 'src/shared/services/api/intendants/intendant.service';
import { UserStateService } from 'src/shared/services/states/UserStateService';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
})
export class NavbarComponent implements OnInit {
  user: UserDataResponse;

  constructor(
    private userStateService: UserStateService,
    public authService: AuthService
  ) {}

  ngOnInit(): void {
    this.user = this.userStateService.currentUser;
  }
}
