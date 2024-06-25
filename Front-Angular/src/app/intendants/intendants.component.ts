import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { Observable } from 'rxjs';
import { ErrorModalComponent } from 'src/shared/modals/error-modal/error-modal.component';
import { IntendantDataResponse } from 'src/shared/models/intendant/intendant.models';
import { IntendantService } from 'src/shared/services/api/intendants/intendant.service';

@Component({
  selector: 'app-intendants',
  templateUrl: './intendants.component.html',
  styleUrls: ['./intendants.component.scss'],
})
export class IntendantsComponent {
  intendant: IntendantDataResponse;
  intendantEmail: string;
  searchForm = new FormGroup({
    email: new FormControl(null, [
      Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$'),
      Validators.required,
    ]),
  });

  constructor(
    private intendantService: IntendantService,
    private dialog: MatDialog
  ) {}

  submitSearch() {
    if (this.searchForm.invalid) {
      this.openErrorModal('Please fill email correctly.');
      return;
    }

    this.intendantService
      .findIntendantByEmail(this.searchForm?.value?.email)
      .subscribe({
        next: (response: IntendantDataResponse) => {
          this.intendant = response;
          this.intendantEmail = null;
        },
        error: (error: any) => {
          if (
            error.status === 404 &&
            error.error.detail === 'No school associated with this email'
          ) {
            this.intendantEmail = this.searchForm?.value?.email;
            this.intendant = null;
          } else {
            console.error('Error:', error);
          }
        },
      });
  }

  openErrorModal(errorMessage: string) {
    this.dialog.open(ErrorModalComponent, {
      data: { errorMessage },
    });
  }
}
