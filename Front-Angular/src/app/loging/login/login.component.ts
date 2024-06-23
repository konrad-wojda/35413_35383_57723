import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { MatDialog } from '@angular/material/dialog';
import { AuthService } from 'src/shared/services/auth.service';
import { ErrorModalComponent } from 'src/shared/modals/error-modal/error-modal.component';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  form = new FormGroup({
    email: new FormControl(null, Validators.required),
    password: new FormControl(null, Validators.required),
  });

  constructor(
    private authService: AuthService,
    private router: Router,
    private dialog: MatDialog
  ) {}

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
          this.openErrorModal(error.error.detail);
        },
      });
  }

  openErrorModal(errorMessage: string) {
    this.dialog.open(ErrorModalComponent, {
      data: { errorMessage },
    });
  }
}
