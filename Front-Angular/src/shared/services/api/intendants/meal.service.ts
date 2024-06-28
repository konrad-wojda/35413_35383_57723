import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { MealResponse } from 'src/shared/models/intendant/meal.models';

@Injectable({
  providedIn: 'root',
})
export class MealService {
  constructor(private http: HttpClient) {}

  getMeals(): Observable<MealResponse[]> {
    return this.http
      .get<MealResponse[]>(`http://127.0.0.1:8000/api/meals/get`)
      .pipe((data) => {
        return data;
      });
  }
}
