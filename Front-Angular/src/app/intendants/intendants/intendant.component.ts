import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { IntendantDataResponse } from 'src/app/models/intendant/user.models';

@Component({
  selector: 'app-intendant',
  templateUrl: './intendant.component.html',
  styleUrls: ['./intendant.component.scss'],
})
export class IntendantComponent implements OnInit {
  @Input() intendant: IntendantDataResponse;

  ngOnInit(): void {
    console.log(this.intendant);
  }
}
