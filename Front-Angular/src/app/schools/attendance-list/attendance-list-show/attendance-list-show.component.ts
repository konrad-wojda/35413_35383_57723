import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  Input,
  OnChanges,
  OnInit,
  SimpleChanges,
} from '@angular/core';
import {
  Observable,
  endWith,
  forkJoin,
  ignoreElements,
  mergeMap,
  of,
} from 'rxjs';
import { AttendanceListResponse } from 'src/shared/models/intendant/attendance-list.models';
import { IntendantDataResponse } from 'src/shared/models/intendant/intendant.models';
import { AttendanceListService } from 'src/shared/services/api/intendants/attendance-list.service';
import { MealService } from 'src/shared/services/api/intendants/meal.service';

@Component({
  selector: 'app-attendance-list-show',
  templateUrl: './attendance-list-show.component.html',
  styleUrls: ['./attendance-list-show.component.scss'],
})
export class AttendanceListShowComponent implements OnInit, OnChanges {
  @Input() formattedDate: string;
  attendanceList$: Observable<AttendanceListResponse[]>;
  displayedColumns: string[];
  dataSource: any[];
  intendantData: IntendantDataResponse;

  constructor(
    private attendanceListService: AttendanceListService,
    private mealService: MealService
  ) {
    this.intendantData = JSON.parse(
      sessionStorage.getItem('IntendantStateService')
    );
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (
      changes['formattedDate'] &&
      changes['formattedDate'].currentValue !==
        changes['formattedDate'].previousValue
    ) {
      this.callApi(changes['formattedDate'].currentValue);
    }
  }
  callApi(date: string) {
    console.log('callApi');

    this.attendanceListService.getAttendanceList(
      this.intendantData.id_school,
      date
    );
  }

  ngOnInit(): void {
    const meals$ = this.mealService.getMeals();
    this.attendanceList$ = this.attendanceListService.getAttendanceList(
      this.intendantData.id_school,
      this.formattedDate
    );
    forkJoin([this.attendanceList$, meals$])
      .pipe(
        mergeMap(([attendanceList, meals]) => {
          this.displayedColumns = [
            'Uczniowie',
            ...meals.map(({ type }) => type),
          ];
          const transformedData = [];
          for (const res of attendanceList) {
            const studentObj: any = {
              [this.displayedColumns[0]]: res?.data[0], // Uczniowie
            };

            for (let i = 1; i < this.displayedColumns?.length; i++) {
              studentObj[this.displayedColumns[i]] = res?.data.includes(i)
                ? 'Obecny'
                : 'Nieobecny';
            }

            transformedData.push(studentObj);
          }
          this.dataSource = transformedData;
          return of(null);
        })
      )
      .subscribe(),
      (error) => {
        console.error('Error fetching data:', error);
      };
  }
}
