import { Component, EventEmitter, Input, OnChanges } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ErrorModalComponent } from 'src/shared/modals/error-modal/error-modal.component';
import {
  AttendanceList,
  AttendanceListRequest,
} from 'src/shared/models/intendant/attendance-list.models';
import { IntendantDataResponse } from 'src/shared/models/intendant/intendant.models';
import { MealResponse } from 'src/shared/models/intendant/meal.models';
import { AttendanceListService } from 'src/shared/services/api/intendants/attendance-list.service';
import { StudentService } from 'src/shared/services/api/intendants/student.service';

@Component({
  selector: 'app-attendance-list-empty',
  templateUrl: './attendance-list-empty.component.html',
  styleUrls: ['./attendance-list-empty.component.scss'],
})
export class AttendanceListEmptyComponent implements OnChanges {
  @Input() formattedDate: string;
  @Input() displayedColumns: string[];
  @Input() meals: MealResponse[];
  // @EventEmitter
  dataSource: any[];
  intendantData: IntendantDataResponse;
  constructor(
    private studentService: StudentService,
    private attendanceListService: AttendanceListService,
    private dialog: MatDialog
  ) {
    this.intendantData = JSON.parse(
      sessionStorage.getItem('IntendantStateService')
    );
  }

  ngOnChanges(): void {
    const transformedData = [];
    this.studentService
      .getStudents(this.intendantData.id_school)
      .subscribe((response) => {
        for (const res of response) {
          const studentObj: any = {
            id_student: res?.id_student,
            [this.displayedColumns[0]]: res?.full_name, // kolumna Uczniowie
          };
          for (let i = 1; i < this.displayedColumns?.length; i++) {
            studentObj[this.displayedColumns[i]] = 'Obecny';
          }

          transformedData.push(studentObj);
        }
        this.dataSource = transformedData;
      });
  }

  toggleValue(button: any, col: string) {
    this.dataSource.map((student) => {
      if (student === button) {
        student[col] = student[col] === 'Obecny' ? 'Nieobecny' : 'Obecny';
      }
    });
  }

  saveAttendance() {
    let attendanceFormatted: AttendanceList[] = [];
    for (const ds of this.dataSource) {
      const mealTypes = [];
      for (const meal of this.meals) {
        if (ds[meal.type] === 'Obecny') mealTypes.push(meal.id_meal_type);
      }

      const studentObj: AttendanceList = {
        id_student: ds['id_student'],
        id_meal_type: mealTypes,
      };
      attendanceFormatted.push(studentObj);
    }

    const payload: AttendanceListRequest = {
      token: '',
      date: this.formattedDate,
      id_school: this.intendantData.id_school,
      attendance_list: attendanceFormatted,
    };

    this.attendanceListService.addSingleDayAttendance(payload).subscribe({
      next: (response: boolean) => {},
      error: (error: any) => {
        this.openErrorModal('Lista obecności nie została zapisana');
      },
    });
  }

  openErrorModal(errorMessage: string) {
    this.dialog.open(ErrorModalComponent, {
      data: { errorMessage },
    });
  }
}
