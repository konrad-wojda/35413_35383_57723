import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-error-modal',
  templateUrl: './error-modal.component.html',
  styleUrls: ['./error-modal.component.scss'],
})
export class ErrorModalComponent {
  constructor(
    @Inject(MAT_DIALOG_DATA) public data: { errorMessage: string },
    private dialogRef: MatDialogRef<ErrorModalComponent>
  ) {
    setTimeout(() => {
      this.dialogRef.close();
    }, 5000);
  }
}
