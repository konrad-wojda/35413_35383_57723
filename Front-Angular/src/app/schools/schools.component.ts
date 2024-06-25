import { Component } from '@angular/core';
import { UserDataResponse } from 'src/shared/models/intendant/user.models';
import { UserStateService } from 'src/shared/services/states/UserStateService';

@Component({
  selector: 'app-schools',
  templateUrl: './schools.component.html',
  styleUrls: ['./schools.component.scss'],
})
export class SchoolsComponent {
  user: UserDataResponse;

  constructor(private userStateService: UserStateService) {}

  ngOnInit(): void {
    this.user = this.userStateService.currentUser;
  }
}
