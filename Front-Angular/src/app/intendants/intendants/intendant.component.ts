import { Component, Input, OnInit } from '@angular/core';
import { IntendantDataResponse } from 'src/shared/models/intendant/intendant.models';

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
