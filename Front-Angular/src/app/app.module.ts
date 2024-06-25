import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { MatDialogModule } from '@angular/material/dialog';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { LoginComponent } from './loging/login/login.component';
import { HomeComponent } from './home/home.component';
import { RegisterComponent } from './loging/register/register.component';
import { UserPageComponent } from './user-page/user-page.component';
import { UserDetailsComponent } from './user-page/user-details/user-details.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AddSchoolComponent } from './schools/add-school/add-school.component';
import { IntendantsComponent } from './intendants/intendants.component';
import { IntendantComponent } from './intendants/intendants/intendant.component';
import { ErrorModalComponent } from 'src/shared/modals/error-modal/error-modal.component';
import { DownloadCSVButtonComponent } from 'src/shared/buttons/download-csv/download-csv.component';
import { AddIntendantToSchoolComponent } from './intendants/add-intendant-to-school/add-intendant-to-school.component';
import { SchoolsComponent } from './schools/schools.component';

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
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    MatDialogModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
