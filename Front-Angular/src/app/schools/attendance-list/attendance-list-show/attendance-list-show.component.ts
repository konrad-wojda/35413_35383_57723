import { Component, Input, OnChanges } from '@angular/core';

import { AttendanceListResponse } from 'src/shared/models/intendant/attendance-list.models';
import { IntendantDataResponse } from 'src/shared/models/intendant/intendant.models';

@Component({
  selector: 'app-attendance-list-show',
  templateUrl: './attendance-list-show.component.html',
  styleUrls: ['./attendance-list-show.component.scss'],
})
export class AttendanceListShowComponent implements OnChanges {
  @Input() formattedDate: string;
  @Input() attendanceList: AttendanceListResponse[];
  @Input() displayedColumns: string[];

  dataSource: any[];
  intendantData: IntendantDataResponse;

  constructor() {
    this.intendantData = JSON.parse(
      sessionStorage.getItem('IntendantStateService')
    );
  }

  ngOnChanges(): void {
    const transformedData = [];
    for (const res of this.attendanceList) {
      const studentObj: any = {
        [this.displayedColumns[0]]: res?.data[0], // kolumna Uczniowie
      };

      for (let i = 1; i < this.displayedColumns?.length; i++) {
        studentObj[this.displayedColumns[i]] = res?.data.includes(i)
          ? 'Obecny'
          : 'Nieobecny';
      }

      transformedData.push(studentObj);
    }
    this.dataSource = transformedData;
  }
}
