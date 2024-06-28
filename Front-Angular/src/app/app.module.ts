import { NgModule } from '@angular/core';
import { MatDialogModule } from '@angular/material/dialog';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatTableModule } from '@angular/material/table';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';

import { DownloadCSVButtonComponent } from 'src/shared/buttons/download-csv/download-csv.component';
import { ErrorModalComponent } from 'src/shared/modals/error-modal/error-modal.component';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { AddIntendantToSchoolComponent } from './intendants/add-intendant-to-school/add-intendant-to-school.component';
import { IntendantsComponent } from './intendants/intendants.component';
import { IntendantComponent } from './intendants/intendants/intendant.component';
import { LoginComponent } from './loging/login/login.component';
import { RegisterComponent } from './loging/register/register.component';
import { NavbarComponent } from './navbar/navbar.component';
import { AddSchoolComponent } from './schools/add-school/add-school.component';
import { AddStudentsComponent } from './schools/add-students/add-students.component';
import { AttendanceListComponent } from './schools/attendance-list/attendance-list.component';
import { SchoolsComponent } from './schools/schools.component';
import { UserDetailsComponent } from './user-page/user-details/user-details.component';
import { UserPageComponent } from './user-page/user-page.component';
import { AttendanceListEmptyComponent } from './schools/attendance-list/attendance-list-empty/attendance-list-empty.component';
import { AttendanceListShowComponent } from './schools/attendance-list/attendance-list-show/attendance-list-show.component';
import { MAT_DATE_LOCALE, MatNativeDateModule } from '@angular/material/core';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    LoginComponent,
    HomeComponent,
    RegisterComponent,
    UserPageComponent,
    UserDetailsComponent,
    IntendantsComponent,
    IntendantComponent,
    AddSchoolComponent,
    SchoolsComponent,
    ErrorModalComponent,
    DownloadCSVButtonComponent,
    AddIntendantToSchoolComponent,
    AddStudentsComponent,
    AttendanceListComponent,
    AttendanceListEmptyComponent,
    AttendanceListShowComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    MatDialogModule,
    MatTableModule,
    MatButtonModule,
    MatDatepickerModule,
    MatFormFieldModule,
    MatNativeDateModule,
    MatInputModule,
  ],
  providers: [{ provide: MAT_DATE_LOCALE, useValue: 'pl-PL' }],
  bootstrap: [AppComponent],
})
export class AppModule {}
