import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Observable } from 'rxjs';
import { IntendantDataResponse } from 'src/shared/models/intendant/intendant.models';
import { IntendantService } from 'src/shared/services/intendants/intendant.service';

@Component({
  selector: 'app-intendants',
  templateUrl: './intendants.component.html',
  styleUrls: ['./intendants.component.scss'],
})
export class IntendantsComponent {
  intendant$: Observable<IntendantDataResponse>;
  searchForm = new FormGroup({
    email: new FormControl(null, [
      Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$'),
      Validators.required,
    ]),
  });

  constructor(private intendantService: IntendantService) {}

  submitSearch() {
    if (this.searchForm.invalid) {
      return;
    }

    this.intendant$ = this.intendantService.findIntendantByEmail(
      this.searchForm?.value?.email
    );
  }
}
