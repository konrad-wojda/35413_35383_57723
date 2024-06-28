import { Component } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';

@Component({
  selector: 'app-attendance-list',
  templateUrl: './attendance-list.component.html',
  styleUrls: ['./attendance-list.component.scss'],
})
export class AttendanceListComponent {
  selectedDate: Date;
  formattedDate: string; // YYYY-MM-DD

  onDateSelected(event: MatDatepickerInputEvent<any, any>): void {
    this.selectedDate = event.value;
    const day = this.selectedDate.getDate().toString().padStart(2, '0');
    const month = (this.selectedDate.getMonth() + 1)
      .toString()
      .padStart(2, '0');
    this.formattedDate = `${this.selectedDate.getFullYear()}-${month}-${day}`;
  }
}
