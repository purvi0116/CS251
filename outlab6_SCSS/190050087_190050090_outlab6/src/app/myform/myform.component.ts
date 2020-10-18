
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Form } from '../userForm';
import { FormService } from '../services/form.service';
import { CommonModule } from '@angular/common';  
import { BrowserModule } from '@angular/platform-browser';

@Component({
  selector: 'app-myform',
  templateUrl: './myform.component.html',
  styleUrls: ['./myform.component.scss']
})
export class  MyformComponent implements OnInit {
  url = 'https://cs251-outlab-6.herokuapp.com/initial_values/';
  public formData : Form;
  errBlock:boolean = false;
  postCalled:boolean=false;
  incom:boolean=false;
  myform = new FormGroup({
    name: new FormControl('',Validators.required),
    email: new FormControl('',[Validators.required,Validators.email,Validators.pattern('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$')]),
    feedback: new FormControl('',Validators.required),
    comment: new FormControl('')
  })
  constructor(private _formService: FormService) { }

  ngOnInit(){
    this._formService.getForm()
    .subscribe(data => this.formData = data)
  }
  onSubmit() {
    // TODO: Use EventEmitter with form value
    
    this._formService.postForm(this.myform) .subscribe((response)=> {
      console.log(response);
      console.log("all good..");
      console.log("value of errBlock is ",this.errBlock);
      this.formData.name = this.myform.get('name').value;
      this.formData.comment = this.myform.get('comment').value;
      this.formData.email = this.myform.get('email').value;
      this.formData.feedback = this.myform.get('feedback').value;
      this.errBlock = false;
      this.postCalled=true;
    },error => {
      this.postCalled=true;
      this.errBlock = true;
      console.log(error);
      console.log("errorrr..");
      
    }  
    );
    //this.router.navigate(['/form']);
    
  }

  closeAlert(){
    this.postCalled=false;
  }

  incomplete(){
    this.incom=true;
  }

  complete(){
    this.incom=false;
  }
  
  
  
}
