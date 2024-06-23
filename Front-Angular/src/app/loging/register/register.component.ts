import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from 'src/shared/services/api.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
})
export class RegisterComponent {
  res = { status_code: 199, detail: '' };

  form = new FormGroup({
    email: new FormControl(null, Validators.required),
    password: new FormControl(null, Validators.required),
    repeat_password: new FormControl(null, Validators.required),
  });
  constructor(private apiService: ApiService, private router: Router) {}

  submitForm() {
    if (this.form.invalid) {
      return;
    }
    this.apiService
      .register(
        this.form.get('email')?.value,
        this.form.get('password')?.value,
        this.form.get('repeat_password').value
      )
      .subscribe(
        (response) => {
          if (response.status_code == 200) {
            this.router.navigate(['/login']); // zmienić redirect na chcesz sie zalogować? jeśli tak, to wyświetli się app-login
            return;
          }
        },
        (error) => {
          this.res.status_code = error.status;
          this.res.detail = error.error.detail;
        }
      );
  }
}
