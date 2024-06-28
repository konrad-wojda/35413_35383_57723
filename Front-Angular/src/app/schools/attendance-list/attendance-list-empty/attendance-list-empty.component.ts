import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ErrorModalComponent } from 'src/shared/modals/error-modal/error-modal.component';
import { IntendantDataResponse } from 'src/shared/models/intendant/intendant.models';
import { AttendanceListService } from 'src/shared/services/api/intendants/attendance-list.service';
import { MealService } from 'src/shared/services/api/intendants/meal.service';
import { StudentService } from 'src/shared/services/api/intendants/student.service';

@Component({
  selector: 'app-attendance-list-empty',
  templateUrl: './attendance-list-empty.component.html',
  styleUrls: ['./attendance-list-empty.component.scss'],
})
export class AttendanceListEmptyComponent implements OnInit {
  ELEMENT_DATA: any[] = [
    { position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H' },
    { position: 2, name: 'Helium', weight: 4.0026, symbol: 'He' },
    { position: 3, name: 'Lithium', weight: 6.941, symbol: 'Li' },
    { position: 4, name: 'Beryllium', weight: 9.0122, symbol: 'Be' },
    { position: 5, name: 'Boron', weight: 10.811, symbol: 'B' },
    { position: 6, name: 'Carbon', weight: 12.0107, symbol: 'C' },
    { position: 7, name: 'Nitrogen', weight: 14.0067, symbol: 'N' },
    { position: 8, name: 'Oxygen', weight: 15.9994, symbol: 'O' },
    { position: 9, name: 'Fluorine', weight: 18.9984, symbol: 'F' },
    { position: 10, name: 'Neon', weight: 20.1797, symbol: 'Ne' },
  ];
  displayedColumns: string[];
  dataSource = this.ELEMENT_DATA;
  intendantData: IntendantDataResponse;

  // form = new FormGroup({
  //   student_first_name: new FormControl(null, Validators.required),
  //   student_last_name: new FormControl(null, Validators.required),
  //   student_class: new FormControl(null, Validators.required),
  // });

  constructor(
    private attendanceListService: AttendanceListService,
    private mealService: MealService,
    private studentService: StudentService,
    private dialog: MatDialog
  ) {}

  ngOnInit(): void {
    this.mealService.getMeals().subscribe((response) => {
      this.displayedColumns = [
        'Uczniowie',
        ...response.map(({ type }) => type),
      ];
    });

    this.studentService.getStudents(1).subscribe((response) => {
      console.log(response);
    });

    this.intendantData = JSON.parse(
      sessionStorage.getItem('IntendantStateService')
    );
    this.attendanceListService
      .getAttendanceList(this.intendantData.id_school)
      .subscribe((response) => {
        console.log(response);
      });
  }

  submitForm() {
    const intendantData: IntendantDataResponse = JSON.parse(
      sessionStorage.getItem('IntendantStateService')
    );

    if (!intendantData.is_main_admin) {
      this.openErrorModal('Nie jesteś administratorem tej szkoły');
      return;
    }

    // if (this.form.invalid) {
    //   this.openErrorModal('Uzupełnij wszystkie pola');
    //   return;
    // }

    // this.studentService
    //   .AddStudentToSchool(
    //     intendantData.id_school,
    //     this.form.get('student_first_name')?.value,
    //     this.form.get('student_last_name')?.value,
    //     this.form.get('student_class')?.value
    //   )
    //   .subscribe({
    //     next: (response) => {},
    //     error: (error) => {
    //       this.openErrorModal(error.error.detail);
    //     },
    //   });
  }

  openErrorModal(errorMessage: string) {
    this.dialog.open(ErrorModalComponent, {
      data: { errorMessage },
    });
  }
}
