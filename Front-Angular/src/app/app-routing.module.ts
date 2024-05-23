import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LoginComponent } from './loging/login/login.component';
import { HomeComponent } from './home/home.component';
import { RegisterComponent } from './loging/register/register.component';
import { UserPageComponent } from './user-page/user-page.component';
import { UserDetailsComponent } from './user-page/user-details/user-details.component';
import { IntendantsComponent } from './intendants/intendants.component';
import { SchoolsComponent } from './schools/schools.component';

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
  },
  {
    path: 'user/edit',
    component: UserDetailsComponent,
  },
  {
    path: 'intendants',
    component: IntendantsComponent,
  },
  {
    path: 'schools',
    component: SchoolsComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
