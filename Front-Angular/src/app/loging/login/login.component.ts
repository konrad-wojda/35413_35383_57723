import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { MatDialog } from '@angular/material/dialog';
import { AuthService } from 'src/shared/services/api/auth.service';
import { ErrorModalComponent } from 'src/shared/modals/error-modal/error-modal.component';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  form = new FormGroup({
    email: new FormControl(null, [
      Validators.required,
      Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$'),
    ]),
    password: new FormControl(null, Validators.required),
  });

  constructor(
    private authService: AuthService,
    private router: Router,
    private dialog: MatDialog
  ) {}

  getErrorMessageEmail() {
    if (this.form.controls.email.hasError('required')) {
      return 'Musisz uzupełnić adres e-mail';
    }

    return this.form.controls.email.hasError('pattern')
      ? 'E-mail jest niepoprawny'
      : '';
  }

  getErrorMessagePassword() {
    return 'Musisz uzupełnić hasło';
  }

  submitForm() {
    if (this.form.invalid) {
      return;
    }
    this.authService
      .login(this.form.get('email')?.value, this.form.get('password')?.value)
      .subscribe({
        next: (response) => {
          this.router.navigate(['/']);
        },
        error: (error) => {
          this.openErrorModal('Logowanie nie powidoło się');
        },
      });
  }

  openErrorModal(errorMessage: string) {
    this.dialog.open(ErrorModalComponent, {
      data: { errorMessage },
    });
  }
}
