import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LoginComponent } from './loging/login/login.component';
import { HomeComponent } from './home/home.component';
import { RegisterComponent } from './loging/register/register.component';
import { UserPageComponent } from './user-page/user-page.component';
import { UserDetailsComponent } from './user-page/user-details/user-details.component';
import { ProductsComponent } from './products/products.component';
import { ProductComponent } from './products/product/product.component';
import { OrdersComponent } from './orders/orders.component';

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
    path: 'products',
    component: ProductsComponent,
  },
  {
    path: 'product',
    component: ProductComponent,
  },
  {
    path: 'orders',
    component: OrdersComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
