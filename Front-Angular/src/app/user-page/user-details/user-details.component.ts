import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UserAdressResponse } from 'src/app/models/response_models';
import { AuthService } from 'src/app/services/auth.service';
import { UsersDataService } from 'src/app/services/users-data.service';
@Component({
  selector: 'app-user-details',
  templateUrl: './user-details.component.html',
  styleUrls: ['./user-details.component.scss'],
})
export class UserDetailsComponent implements OnInit {
  editingEmail: boolean = false;
  editingFirst: boolean = false;
  editingLast: boolean = false;
  editingPhone: boolean = false;
  editingPost: boolean = false;
  editingStreetName: boolean = false;
  editingStreetNumber: boolean = false;
  editingFlat: boolean = false;
  user: UserAdressResponse;

  properties: any[];

  form = new FormGroup({
    email: new FormControl(
      null,
      Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$')
    ),
    first_name: new FormControl(null),
    last_name: new FormControl(null),
    telephone: new FormControl(null),
    post_code: new FormControl(null),
    street_name: new FormControl(null),
    street_number: new FormControl(null),
    flat_number: new FormControl(null),
    hashed_password: new FormControl(null),
  });

  constructor(
    private usersDataService: UsersDataService,
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
      body['telephone'] = this.form.controls.telephone.value;
    }
    if (this.properties[4].isVisible) {
      body['post_code'] = this.form.controls.post_code.value;
    }
    if (this.properties[5].isVisible) {
      body['street_name'] = this.form.controls.street_name.value;
    }
    if (this.properties[6].isVisible) {
      body['street_number'] = this.form.controls.street_number.value;
    }
    if (this.properties[7].isVisible) {
      body['flat_number'] = this.form.controls.flat_number.value;
    }
    if (this.properties[8].isVisible) {
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
      case 'editingPhone': {
        this.properties[3].isVisible = !this.properties[3].isVisible;
        break;
      }
      case 'editingPost': {
        this.properties[4].isVisible = !this.properties[4].isVisible;
        break;
      }
      case 'editingStreetName': {
        this.properties[5].isVisible = !this.properties[5].isVisible;
        break;
      }
      case 'editingStreetNumber': {
        this.properties[6].isVisible = !this.properties[6].isVisible;
        break;
      }
      case 'editingFlat': {
        this.properties[7].isVisible = !this.properties[7].isVisible;
        break;
      }
      case 'hashed_password': {
        this.properties[8].isVisible = !this.properties[8].isVisible;
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
          label: 'Telephone number',
          editingName: 'editingPhone',
          isVisible: false,
          type: 'number',
          placeholder: this.user.telephone,
          formControlName: 'telephone',
        },
        {
          label: 'Post code',
          editingName: 'editingPost',
          isVisible: false,
          type: 'number',
          placeholder: this.user.post_code,
          formControlName: 'post_code',
        },
        {
          label: 'Street name',
          editingName: 'editingStreetName',
          isVisible: false,
          type: 'text',
          placeholder: this.user.street_name,
          formControlName: 'street_name',
        },
        {
          label: 'Street number',
          editingName: 'editingStreetNumber',
          isVisible: false,
          type: 'number',
          placeholder: this.user.street_number,
          formControlName: 'street_number',
        },
        {
          label: 'Flat number',
          editingName: 'editingFlat',
          isVisible: false,
          type: 'number',
          placeholder: this.user.flat_number,
          formControlName: 'flat_number',
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
