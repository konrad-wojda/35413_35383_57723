import { Component, Input } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { ErrorModalComponent } from 'src/shared/modals/error-modal/error-modal.component';
import { IntendantDataResponse } from 'src/shared/models/intendant/intendant.models';
import { StudentService } from 'src/shared/services/api/intendants/student.service';

@Component({
  selector: 'app-add-students',
  templateUrl: './add-students.component.html',
  styleUrls: ['./add-students.component.scss'],
})
export class AddStudentsComponent {
  @Input() intendantEmail: string;

  form = new FormGroup({
    student_first_name: new FormControl(null, Validators.required),
    student_last_name: new FormControl(null, Validators.required),
    student_class: new FormControl(null, Validators.required),
  });

  constructor(
    private studentService: StudentService,
    private router: Router,
    private dialog: MatDialog
  ) {}

  submitForm() {
    const intendantData: IntendantDataResponse = JSON.parse(
      sessionStorage.getItem('IntendantStateService')
    );

    if (!intendantData.is_main_admin) {
      this.openErrorModal('Nie jesteś administratorem tej szkoły');
      return;
    }

    if (this.form.invalid) {
      this.openErrorModal('Uzupełnij wszystkie pola');
      return;
    }

    this.studentService
      .AddStudentToSchool(
        intendantData.id_school,
        this.form.get('student_first_name')?.value,
        this.form.get('student_last_name')?.value,
        this.form.get('student_class')?.value
      )
      .subscribe({
        next: (response) => {},
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
