import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {ContactComponent} from './contact/contact.component'
import {MyformComponent} from './myform/myform.component'
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

const routes: Routes = [
  {path:'contact', component:ContactComponent},
  {path:'form', component:MyformComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes),BrowserModule,FormsModule, ReactiveFormsModule],
  exports: [RouterModule],
  declarations: [
    ContactComponent,
    MyformComponent
  ]
})
export class AppRoutingModule { }
//redirect after submit to form page but with modified
//Comment may not be mandatory
//if wrong email type it