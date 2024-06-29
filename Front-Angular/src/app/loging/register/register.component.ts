import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { ErrorModalComponent } from 'src/shared/modals/error-modal/error-modal.component';
import { ApiService } from 'src/shared/services/api/api.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
})
export class RegisterComponent {
  res = { status_code: 199, detail: '' };

  form = new FormGroup({
    email: new FormControl(null, [
      Validators.required,
      Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$'),
    ]),
    password: new FormControl(null, Validators.required),
    repeat_password: new FormControl(null, Validators.required),
  });

  constructor(
    private apiService: ApiService,
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

  getErrorMessageRepPassword() {
    return 'Musisz uzupełnić hasło';
  }

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
          this.openErrorModal(
            'Hasła są różne lub ma mniej niż 8 znaków. Hasło powinno zawierać małą, wielką literę, cyfrę oraz znak specjalny.'
          );
        }
      );
  }

  openErrorModal(errorMessage: string) {
    this.dialog.open(ErrorModalComponent, {
      data: { errorMessage },
    });
  }
}
