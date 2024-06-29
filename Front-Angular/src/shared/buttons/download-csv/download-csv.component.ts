import { HttpClient } from '@angular/common/http';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-download-csv-button',
  templateUrl: './download-csv.component.html',
  styleUrls: ['./download-csv.component.scss'],
})
export class DownloadCSVButtonComponent {
  @Input() id_school: number;
  @Input() date: string;
  constructor(private http: HttpClient) {}

  downloadCsv() {
    const token = localStorage.getItem('token');

    this.http
      .get(
        `http://127.0.0.1:8000/api/attendance-list/get-file?token=${token}&date=${this.date}&id_school=${this.id_school}`,
        {
          responseType: 'blob',
        }
      )
      .subscribe((response: Blob) => {
        const utf8Blob = new Blob(['\ufeff', response], {
          type: 'text/csv;charset=utf-8',
        });

        const url = window.URL.createObjectURL(utf8Blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `${this.date}_attendance-list.csv`;

        link.click();
        window.URL.revokeObjectURL(url);
      });
  }
}
