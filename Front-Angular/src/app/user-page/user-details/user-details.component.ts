import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UserDataResponse } from 'src/shared/models/intendant/user.models';
import { AuthService } from 'src/shared/services/auth.service';
import { UserService } from 'src/shared/services/intendants/user.service';
@Component({
  selector: 'app-user-details',
  templateUrl: './user-details.component.html',
  styleUrls: ['./user-details.component.scss'],
})
export class UserDetailsComponent implements OnInit {
  editingEmail: boolean = false;
  editingFirst: boolean = false;
  editingLast: boolean = false;
  user: UserDataResponse;

  properties: any[];

  form = new FormGroup({
    email: new FormControl(
      null,
      Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$')
    ),
    first_name: new FormControl(null),
    last_name: new FormControl(null),
    hashed_password: new FormControl(null),
  });

  constructor(
    private usersDataService: UserService,
    private authService: AuthService,
    private router: Router
  ) {}

  submitForm() {
    let body: Object = {};
    Object.entries(this.properties).forEach((entry) => {
      const [key, value] = entry;
      if (value.isVisible) {
        this.properties[key].formControlName +
          this.form.controls[this.properties[key].formControlName].value;
      }
    });

    if (this.form.invalid) {
      return;
    }
    if (this.properties[0].isVisible) {
      body['email'] = this.form.controls.email.value;
    }
    if (this.properties[1].isVisible) {
      body['first_name'] = this.form.controls.first_name.value;
    }
    if (this.properties[2].isVisible) {
      body['last_name'] = this.form.controls.last_name.value;
    }
    if (this.properties[3].isVisible) {
      body['hashed_password'] = this.form.controls.hashed_password.value;
    }
    this.authService.editUser(body);
    this.router.navigate(['/user']);
  }

  reverse(editingName: String) {
    switch (editingName) {
      case 'editingEmail': {
        this.properties[0].isVisible = !this.properties[0].isVisible;
        break;
      }
      case 'editingFirst': {
        this.properties[1].isVisible = !this.properties[1].isVisible;
        break;
      }
      case 'editingLast': {
        this.properties[2].isVisible = !this.properties[2].isVisible;
        break;
      }
      case 'hashed_password': {
        this.properties[3].isVisible = !this.properties[3].isVisible;
        break;
      }
    }
  }

  ngOnInit(): void {
    this.usersDataService.getData().subscribe((data) => {
      this.user = { ...data };
      this.properties = [
        {
          label: 'E-mail',
          editingName: 'editingEmail',
          isVisible: false,
          type: 'email',
          placeholder: this.user.email,
          formControlName: 'email',
        },
        {
          label: 'First name',
          editingName: 'editingFirst',
          isVisible: false,
          type: 'text',
          placeholder: this.user.first_name,
          formControlName: 'first_name',
        },
        {
          label: 'Last name',
          editingName: 'editingLast',
          isVisible: false,
          type: 'text',
          placeholder: this.user.last_name,
          formControlName: 'last_name',
        },
        {
          label: 'Password',
          editingName: 'hashed_password',
          isVisible: false,
          type: 'password',
          placeholder: '',
          formControlName: 'hashed_password',
        },
      ];
    });
  }
}
