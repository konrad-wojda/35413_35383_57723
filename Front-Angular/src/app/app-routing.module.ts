import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LoginComponent } from './loging/login/login.component';
import { HomeComponent } from './home/home.component';
import { RegisterComponent } from './loging/register/register.component';
import { UserPageComponent } from './user-page/user-page.component';
import { UserDetailsComponent } from './user-page/user-details/user-details.component';
import { IntendantsComponent } from './intendants/intendants.component';
import { SchoolsComponent } from './schools/schools.component';
import { AuthGuard } from '../shared/guards/auth.guard';
import { IntendantGuard } from 'src/shared/guards/intendant.guard';
import { AddStudentsComponent } from './schools/add-students/add-students.component';
import { AttendanceListComponent } from './schools/attendance-list/attendance-list.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  {
    path: 'login',
    component: LoginComponent,
  },
  { path: 'register', component: RegisterComponent },
  {
    path: 'user',
    component: UserPageComponent,
    canActivate: [AuthGuard],
  },
  {
    path: 'user/edit',
    component: UserDetailsComponent,
    canActivate: [AuthGuard],
  },
  {
    path: 'intendants',
    component: IntendantsComponent,
    canActivate: [AuthGuard],
  },
  {
    path: 'schools',
    component: SchoolsComponent,
    canActivate: [AuthGuard],
  },
  {
    path: 'students',
    component: AddStudentsComponent,
    canActivate: [IntendantGuard],
  },
  {
    path: 'attendance-list',
    component: AttendanceListComponent,
    canActivate: [IntendantGuard],
  },
  { path: '**', redirectTo: '' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
