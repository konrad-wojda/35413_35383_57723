import { Component, Input } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { ErrorModalComponent } from 'src/shared/modals/error-modal/error-modal.component';
import { IntendantService } from 'src/shared/services/api/intendants/intendant.service';

@Component({
  selector: 'app-add-intendant-to-school',
  templateUrl: './add-intendant-to-school.component.html',
  styleUrls: ['./add-intendant-to-school.component.scss'],
})
export class AddIntendantToSchoolComponent {
  @Input() intendantEmail: string;

  addIntendantForm = new FormGroup({
    id_school: new FormControl(null, Validators.required),
  });

  constructor(
    private intendantService: IntendantService,
    private router: Router,
    private dialog: MatDialog
  ) {}

  submitForm() {
    if (this.addIntendantForm.invalid) {
      return;
    }

    this.intendantService
      .registerAdminToSchool(
        this.addIntendantForm.get('id_school')?.value,
        this.intendantEmail
      )
      .subscribe({
        next: (response) => {
          // this.router.navigate(['/']);
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
