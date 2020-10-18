import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {ContactComponent} from './contact/contact.component'
import {MyformComponent} from './myform/myform.component'
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {HomeComponent} from './home/home.component'
import { CommonModule } from '@angular/common';

const routes: Routes = [
  {path:'contact', component:ContactComponent},
  {path:'form', component:MyformComponent},
  {path:'home', component:HomeComponent},
  { path: '**', redirectTo: 'contact' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes),BrowserModule,FormsModule, ReactiveFormsModule, CommonModule],
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