import { Component, OnInit } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';
import { AttendanceListResponse } from 'src/shared/models/intendant/attendance-list.models';
import { IntendantDataResponse } from 'src/shared/models/intendant/intendant.models';
import { MealResponse } from 'src/shared/models/intendant/meal.models';
import { AttendanceListService } from 'src/shared/services/api/intendants/attendance-list.service';
import { MealService } from 'src/shared/services/api/intendants/meal.service';

@Component({
  selector: 'app-attendance-list',
  templateUrl: './attendance-list.component.html',
  styleUrls: ['./attendance-list.component.scss'],
})
export class AttendanceListComponent implements OnInit {
  selectedDate: Date;
  formattedDate: string; // YYYY-MM-DD
  displayedColumns: string[] = [];
  meals: MealResponse[];

  attendanceList: AttendanceListResponse[];
  intendantData: IntendantDataResponse;

  constructor(
    private attendanceListService: AttendanceListService,
    private mealService: MealService
  ) {
    this.intendantData = JSON.parse(
      sessionStorage.getItem('IntendantStateService')
    );
  }

  ngOnInit(): void {
    this.mealService.getMeals().subscribe((meals) => {
      this.meals = meals;
      this.displayedColumns = ['Uczniowie', ...meals.map(({ type }) => type)];
    });
  }

  onDateSelected(event: MatDatepickerInputEvent<any, any>): void {
    this.selectedDate = event.value;
    const day = this.selectedDate.getDate().toString().padStart(2, '0');
    const month = (this.selectedDate.getMonth() + 1)
      .toString()
      .padStart(2, '0');
    this.formattedDate = `${this.selectedDate.getFullYear()}-${month}-${day}`;

    this.attendanceListService
      .getAttendanceList(this.intendantData.id_school, this.formattedDate)
      .subscribe((response) => {
        this.attendanceList = response;
      });
  }
}
