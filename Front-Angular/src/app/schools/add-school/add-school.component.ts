import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { ErrorModalComponent } from 'src/shared/modals/error-modal/error-modal.component';
import { SchoolData } from 'src/shared/models/intendant/school.models';
import { SchoolService } from 'src/shared/services/api/intendants/school.service';

@Component({
  selector: 'app-add-school',
  templateUrl: './add-school.component.html',
  styleUrls: ['./add-school.component.scss'],
})
export class AddSchoolComponent {
  properties: any[];

  form = new FormGroup({
    name_of_school: new FormControl('', [
      Validators.minLength(5),
      Validators.required,
    ]),
    post_code: new FormControl(null, [
      Validators.pattern(/^\d{2}-\d{3}$/),
      Validators.required,
    ]),
    street_name: new FormControl('', [
      Validators.minLength(2),
      Validators.required,
    ]),
    street_number: new FormControl<number>(null, [
      Validators.min(1),
      Validators.max(10000),
      Validators.required,
    ]),
  });

  constructor(
    private schoolService: SchoolService,
    private dialog: MatDialog
  ) {}

  submitForm() {
    if (this.form.invalid) {
      for (const key of Object.keys(this.form.controls)) {
        if (this.form.controls[key].status === 'INVALID') {
          this.openErrorModal(key);
          return;
        }
      }
      this.openErrorModal('Nieprzewidziany błąd');
      return;
    }

    this.form.value.post_code = Number(
      this.form.value.post_code.replace('-', '')
    );

    this.schoolService.createSchool(this.form.value as SchoolData);
  }

  ngOnInit(): void {
    this.properties = [
      {
        label: 'Nazwa szkoły',
        type: 'text',
        placeholder: 'nazwa szkoły',
        formControlName: 'name_of_school',
      },
      {
        label: 'Kod pocztowy',
        type: 'text',
        placeholder: '00-000',
        formControlName: 'post_code',
      },
      {
        label: 'Nazwa ulicy',
        type: 'text',
        placeholder: 'nazwa ulicy',
        formControlName: 'street_name',
      },
      {
        label: 'Numer budynku',
        type: 'number',
        placeholder: 'numer domu',
        formControlName: 'street_number',
      },
    ];
  }

  openErrorModal(errorMessage: string) {
    this.dialog.open(ErrorModalComponent, {
      data: { errorMessage },
    });
  }
}
